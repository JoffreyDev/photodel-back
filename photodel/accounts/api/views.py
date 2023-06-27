from rest_framework import generics, permissions, status, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from accounts.models import Profile, VerificationCode, ProCategory, Specialization, TeamInvites, \
    ProfileComment, ProfileLike, ProfileFavorite, Notifications
from rest_framework_simplejwt.views import TokenViewBase
import accounts.models
from services.accounts_service import check_email_verification_code, update_or_create_verification_token, \
    create_random_code, check_is_unique_email, return_user_use_reset_token, custom_paginator, create_notification
from services.ip_service import get_ip
from services.search_profile_service import filter_by_all_parameters
from services.gallery_service import is_unique_favorite, is_unique_like, filter_queryset_by_param
from tasks.accounts_task import task_send_email_to_user, task_send_reset_password_to_email
from .serializers import ProfileUpdateSerializer, ChangePasswordSerializer, \
    ProCategoryListSerializer, SpecializationListSerializer, \
    ProfilePrivateSerializer, ProfilePublicSerializer, ProfileFavoriteCreateSerializer, \
    ProfileFavoriteListSerializer, ProfileLikeCreateSerializer, ProfileCommentCreateSerializer, \
    ProfileCommentListSerializer, ProfilListSerializer, ProfileForPublicSerializer, ProfilListForMapSerializer, TeamInviteSerializer, ProfileTeamInvitesListSerializer, TeamInviteChangeSerializer, ProfileTeamListSerializer, NotificationsSerializer, HistorySerializer

from .serializers import UserRegisterSerializer, UserSerializer, CustomJWTSerializer
from services.team_service import update_team_invite_status
import logging
import uuid
from yookassa import Configuration, Payment
import json
import datetime

Configuration.account_id = '319943'
Configuration.secret_key = 'test_Q2RQicRBamSd-wo9QtoyKuTn8u3Mh_h8aijtj09crwo'





logger = logging.getLogger(__name__)


class CustomTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = CustomJWTSerializer


class RegisterAPIView(generics.CreateAPIView):
    """
    Класс для регистрации пользователя и создание его профиля автоматически
    """
    queryset = User
    serializer_class = UserRegisterSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class RetrieveUserAPIView(generics.RetrieveAPIView):
    """
    Класс для получение токенов для пользователя при авторизации
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VerificationEmailViewSet(viewsets.ViewSet):
    """
    Верификация email
    Класс для отсыла верификациооных кодов для эмейлов и проверки правильный ли код был введен
    """
    permission_classes_by_action = {
        'send_email': [permissions.IsAuthenticated, ],
    }

    def send_email(self, request):
        """
        Функция получает email отправленный post запросом,
        отсылает на данный email код, и записывает данный код в таблицу VerificationCode
        если email не найден - 400 ошибка
        """
        profile = Profile.objects.get(user=request.user)
        logger.info(f'Пользователь {request.user} хочет потвердить почту')
        code = create_random_code(30)
        update_or_create_verification_token(
            profile, code, type_action='verify')
        logger.info(
            f'Код верификации емейла для пользователя {request.user} сохранен')
        if not task_send_email_to_user(profile.email, code):
            logger.info(
                f'Емейл для пользователя {request.user} не был отправлен')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'E-mail не был найден'})
        logger.info(
            f'Емейл для пользователя {request.user} был успешно отправлен')
        return Response(status=status.HTTP_200_OK, data={"message": 'Код успешно отправлен вам на E-mail'})

    def verify_email(self, request):
        """
        Функция получает код post запросом и токен пользователя
        Сравнивает полученный код и код записанный в таблице VerificationCode и возвращает статус 200
        если коды совпадают и статус 400 - если коды не совпали
        """
        logger.info(
            f'Пользователь {request.user} вводит код для подтвеждения емейла ')
        try:
            code = request.data.get('code', '')
            if check_email_verification_code(code):
                logger.info(
                    f'Пользователь {request.user} успешно подтвердил почту ')
                return Response(status=status.HTTP_200_OK, data={"message": 'Ваш email успешно верефицирован'})
            logger.info(f'Пользователь {request.user} не подтвердил почту ')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":
                                                                      'Введенный код неверный. Попробуйте еще раз'})
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Пользователь не был найден"})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ChangePasswordView(viewsets.ViewSet):
    permission_classes_by_action = {
        'update_password': [permissions.IsAuthenticated, ],
    }

    def update_password_after_reset(self, request):
        """
        Обновление пароля для авторизированного юзера
        """
        ip = get_ip(request)
        logger.info(f'Обновление пароля для пользователя {ip}')
        user = return_user_use_reset_token(request.data.get('token', ''))
        serializer = ChangePasswordSerializer(
            data=request.data, context={'user': user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пароль для пользователя {ip} был сохранен')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пароль для пользователя {ip} не был изменен')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Ваш пароль не был изменен. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def generate_token_for_reset_password(self, request):
        """
        Функция восстановления пароля. После отправки запроса
        генерируется новый рандомный пароль и присваиватся юзеру
        с указанным логином. Данный код отсылается на указанную почту
        """
        try:
            username = request.data.get('username', '')
            logger.info(
                f'Отправка токена для восстановление пароля для пользователя {username} по емейл ')
            profile = Profile.objects.get(user__username=username)
            token = create_random_code(30)
            update_or_create_verification_token(
                profile, token, type_action='reset')
            if task_send_reset_password_to_email(profile.email, token):
                logger.info(
                    f'Токен для пользователя {username} был успешно отправлен на емейл')
                return Response(status=status.HTTP_200_OK, data={"message": 'Ссылка с восстановлением пароля '
                                                                            'успешно отправлена '})
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Токен не был отправлен. '
                                                                                 'Пожалуйства обратитесь в поддержку'})
        except Profile.DoesNotExist:
            logger.error(f'Пользователь не был найден')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Пользовтаель не был найден'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CategoriesProfileViewSet(viewsets.ViewSet):

    def list_specialization(self, request):
        """
        Список категория профи
        """
        ip = get_ip(request)
        instance = Specialization.objects.order_by('name_spec')
        logger.info(
            f'Для пользователя {ip} был получен список профи категорий')
        serializer = SpecializationListSerializer(instance, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_pro_categories(self, request):
        """
        Список специализаий фотографов и моделей
        """
        ip = get_ip(request)
        instance = ProCategory.objects.order_by('name_category')
        logger.info(f'Для пользователя {ip} был получен список специализаий')
        serializer = ProCategoryListSerializer(instance, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProfileViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'partial_update': [permissions.IsAuthenticated, ],
        'private_profile': [permissions.IsAuthenticated, ],
    }

    def private_profile(self, request):
        instance = Profile.objects.get(user=request.user)
        serializer = ProfilePrivateSerializer(instance)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def public_profile(self, request, pk):
        try:
            instance = Profile.objects.get(id=pk)
            serializer = ProfileForPublicSerializer(instance)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Профиль не был найден.'})

    def partial_update(self, request):
        """
        Частитичное или полное обновление полей в таблицу Profile
        """
        user = request.user
        check_is_unique_email(request.data.get('email'), user)
        instance = Profile.objects.get(user=user)
        logger.info(
            f'Обновление профиля для пользователя {user} было запрошено')
        serializer = ProfileUpdateSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(
                f'Обновление профиля для пользователя {user} был выполнено')
            return Response(status=status.HTTP_200_OK, data={"message": 'Обнввление профиля прошло успешно'})
        logger.error(
            f'Обновление профиля для пользователя {user} не было завершено')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Обновление не было выполнено '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def list_profiles(self, request):
        """
        Список профилей для поиска с пагинацией
        """
        user = request.user
        queryset = Profile.objects.filter(status=2, is_hide=False)
        if request.user.is_authenticated:
            profiles = queryset.exclude(user=user)
        else:
            profiles = queryset
        queryset_filter = filter_by_all_parameters(profiles, request.GET) \
            .select_related('user', 'type_pro') \
            .prefetch_related('spec_model_or_photographer')
        queryset_sort = filter_queryset_by_param(queryset_filter,
                                                 request.GET.get(
                                                     'sort_type', ''),
                                                 request.GET.get('filter_field', ''))
        queryset = custom_paginator(queryset_sort, request)
        serializer = ProfilListSerializer(queryset, many=True,
                                          context={'user_coords': request.GET.get('user_coords')})
        return Response(status=status.HTTP_200_OK, data=serializer.data,
                        headers={'Count-Filter-Items': len(queryset_filter)})

    def list_profiles_for_map(self, request):
        """
        Список профилей для карта без пагинации
        """
        profiles = Profile.objects.filter(status=2, is_hide=False)
        queryset = filter_by_all_parameters(profiles, request.GET) \
            .select_related('user', 'type_pro') \
            .prefetch_related('spec_model_or_photographer')
        serializer = ProfilListForMapSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def popular_profiles(self, request):
        """
        Частитичное или полное обновление полей в таблицу Profile
        """
        category = request.GET.get('category')
        if category:
            profiles = Profile.objects.filter(
                is_hide=False, type_pro__name_category=category)[:10]
        else:
            profiles = Profile.objects.filter(is_hide=False)[:10]
        serializer = ProfilePublicSerializer(profiles, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ProfileFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список избранных профилей')
        favorites = ProfileFavorite.objects.filter(sender_favorite_id=pk)
        queryset = filter_queryset_by_param(favorites,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', '')) \
            .select_related('sender_favorite__user', 'sender_favorite__type_pro',
                            'receiver_favorite__user', 'receiver_favorite__type_pro') \
            .prefetch_related('sender_favorite__spec_model_or_photographer',
                              'receiver_favorite__spec_model_or_photographer')

        serializer = ProfileFavoriteListSerializer(queryset, many=True,
                                                   context={'user_coords': request.GET.get('user_coords')})
        logger.info(
            f'Пользователь {request.user} успешно получил список профилей')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(
            f'Пользователь {request.user} хочет добавить профиль в избранное')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_favorite(request.data.get('receiver_favorite'), profile, 'profile'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":
                                                                      'Такой профиль уже есть в избранном'})
        serializer = ProfileFavoriteCreateSerializer(
            data=request.data | {"sender_favorite": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(
                f'Пользователь {request.user} успешно добавил профиль в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил профиль в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request):
        try:
            logger.info(
                f'Пользователь {request.user} хочет удалить профиль из избранного')
            profile_favorites = request.data.get('profile_favorites')
            profile = Profile.objects.get(user=request.user)
            for profile_favorite in profile_favorites:
                instance = ProfileFavorite.objects.get(
                    sender_favorite=profile, receiver_favorite=profile_favorite)
                instance.delete()
            logger.info(
                f'Пользователь {request.user} успешно удалил профиль из избранного')
            return Response(status=status.HTTP_200_OK)
        except ProfileFavorite.DoesNotExist:
            logger.error(
                f'Для Пользователя {request.user} не было найдено избраннйы профиль при удалении')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Избранный профиль не было найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ProfileLikeViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_like': [permissions.IsAuthenticated, ],
        'delete_like': [permissions.IsAuthenticated, ],
    }

    def create_like(self, request):
        logger.info(
            f'Пользователь {request.user} хочет добавить лайк к профилю')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_like(request.data.get('receiver_like'), profile, 'profile'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Лайк профилю уже есть'})
        serializer = ProfileLikeCreateSerializer(
            data=request.data | {"sender_like": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(
                f'Пользователь {request.user} успешно добавил лайк к профилю')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил лайк к профилю')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(
                f'Пользователь {request.user} хочет убрать лайк с профиля')
            profile = Profile.objects.get(user=request.user)
            instance = ProfileLike.objects.get(
                sender_like=profile, receiver_like=pk)
            instance.delete()
            logger.info(
                f'Пользователь {request.user} успешно убрал лайк с профиля')
            return Response(status=status.HTTP_200_OK)
        except ProfileLike.DoesNotExist:
            logger.error(
                f'Для Пользователя {request.user} не было найдено профиля при удалении лайка')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Место съемки не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ProfileCommentViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_comments(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список профилей')
        queryset = ProfileComment.objects.filter(receiver_comment=pk) \
            .select_related('sender_comment', 'receiver_comment')
        serializer = ProfileCommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        logger.info(
            f'Пользователь {request.user} хочет создать комментарий к профилю')
        profile = Profile.objects.get(user=request.user).id
        serializer = ProfileCommentCreateSerializer(
            data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(
                f'Пользователь {request.user} успешно добавил комментарий к профилю')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил комментарий к профилю')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ProfileTeamViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'send_team_invite': [permissions.IsAuthenticated, ],
        'incoming_invites_list': [permissions.IsAuthenticated, ],
        'outgoing_invites_list': [permissions.IsAuthenticated, ],
        'change_invite_status': [permissions.IsAuthenticated, ],
    }

    def send_team_invite(self, request):
        logger.info(
            f'Пользователь {request.user} хочет отправить приглашение в команду')
        sender_profile_instance = Profile.objects.get(
            user=request.data.get('invite_sender'))
        receiver_profile_instance = Profile.objects.get(
            user=request.data.get('invite_receiver'))
        serializer = TeamInviteSerializer(
            data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(sender_profile=sender_profile_instance, receiver_profile=receiver_profile_instance,
                                type='NEW_TEAM_REQUEST', action_position=0)
            logger.info(
                f'Пользователь {request.user} успешно создал приглашение в команду')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не создал запрос')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": 'Cоздание приглашения не было выполнено.'
                                                                  ' Пожалуйства обратитесь в поддержку'})

    def incoming_invites_list(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список приглашений в команду')
        queryset = TeamInvites.objects.filter(invite_sender=pk) \
            .select_related('invite_sender')
        serializer = ProfileTeamInvitesListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def outgoing_invites_list(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список приглашений в команду')
        queryset = TeamInvites.objects.filter(invite_receiver=pk) \
            .select_related('invite_receiver')
        serializer = ProfileTeamInvitesListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def change_invite_status(self, request):
        logger.info(
            f'Пользователь {request.user} хочет изменить статус приглашения в команду')
        profile = Profile.objects.get(user=request.user).id
        serializer = TeamInviteChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        response = update_team_invite_status(
            data=serializer_data, user=request.user)
        if request.data.get('status') == 'ACCEPTED':
            invite = TeamInvites.objects.filter(
                id=request.data.get('request_id')).first()
            sender_profile = Profile.objects.get(
                user=invite.invite_sender.user)
            receiver = Profile.objects.get(
                user=invite.invite_receiver.user)
            sender_profile.team.add(receiver)
        return Response(*response)

    def team_list(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список членов команды')
        queryset = Profile.objects.filter(pk=pk).first().team
        serializer = ProfileTeamListSerializer(queryset, many=True,   context={
                                               'user_coords': request.GET.get('user_coords')})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileNotificationViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_notifications(self, request):
        instance = Profile.objects.get(user=request.user)
        queryset = Notifications.objects.filter(
            receiver_profile=instance, readen=False)
        serializer = NotificationsSerializer(
            queryset, many=True, context={'obj': instance})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def read_notifications(self, request):
        notifications = Notifications.objects.all()
        for notification in request.data.get('notifications'):
            notification_instance = notifications.get(id=notification)
            notification_instance.readen = True
            notification_instance.save()
        return Response(status=status.HTTP_200_OK)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
        
class SubscriptionPay(viewsets.ViewSet):
     
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }
    
    def create_new_payment(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        payment = Payment.create({
        "amount": {
            "value": request.data.get('amount'),
            "currency": "RUB"
        },
        "receipt": {
            "customer": {
                "email": f'{profile.email}'
            }
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://88.214.236.178/profile/finance/?confirm=pending"
        },
        "capture": True,
        "description": f'Оплата подписки {request.data.get("plan")} на {request.data.get("duration")}'
        })

        
     
        payment_data = json.loads(payment.json())
        payment_id = payment_data['id']
        accounts.models.Payment.objects.create(payment_id=payment_data['id'], account=profile, plan=request.data.get('plan'), duration=request.data.get('duration'), value=request.data.get('amount'), status='pending')
        payment_url = (payment_data['confirmation'])['confirmation_url']

        return Response({'confirmation_url': payment_url})
    
    def check_payment(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        payment = accounts.models.Payment.objects.filter(account=profile).last()
       
        info = json.loads((Payment.find_one(payment.payment_id)).json())

        if info['status'] == 'succeeded' and not payment.realized:
            if payment.plan == 'standart':
                profile.pro_account = 1
                profile.pro_subscription_expiration += datetime.timedelta(days=30 * payment.duration)
                profile.save()
                payment.realized = True
                payment.status = 'succeeded'
                payment.save()
                return Response({'Подписка успешно приобретена!'})
            elif payment.plan == 'max':
                 profile.pro_account = 2
                 profile.pro_subscription_expiration += datetime.timedelta(days=30 * payment.duration)
                 profile.save()
                 payment.realized = True
                 payment.save()
                 return Response({'Подписка успешно приобретена!'})
        elif info['status'] != 'succeeded' and info['status'] != 'pending':
              payment.status = 'canceled'
              payment.save()
              return Response({'Платеж не прошел. Вам могут помочь у нас в поддержке.'})
        
    def get_history(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        payments = accounts.models.Payment.objects.filter(account=profile)
        serializer = HistorySerializer(payments, many=True)
        return Response({'payments': serializer.data})
        

   