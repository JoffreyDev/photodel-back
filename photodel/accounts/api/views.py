from rest_framework import generics, permissions, status, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from accounts.models import Profile, VerificationCode, ProCategory, Specialization, \
    Album, Gallery, GalleryImage, GalleryComment, GalleryLike, GalleryFavorite
from rest_framework_simplejwt.views import TokenViewBase
from services.accounts_service import check_email_verification_code, update_or_create_verification_token, \
    create_random_code, check_is_unique_email, return_user_use_reset_token, custom_paginator, \
    is_unique_favorite, is_unique_like, protection_cheating_views, add_view
from services.ip_service import get_ip
from services.search_profile_service import filter_by_all_parameters

from tasks.accounts_task import task_send_email_to_user, task_send_reset_password_to_email
from .serializers import ProfileUpdateSerializer, ChangePasswordSerializer, \
    ProCategoryListSerializer, SpecializationListSerializer, AlbumListSerializer, \
    AlbumCreateSerializer, GalleryListSerializer, GalleryForCardListSerializer, \
    ProfilePrivateSerializer, ProfilePublicSerializer, GalleryCreateSerializer, \
    GalleryFavoriteCreateSerializer, GalleryFavoriteListSerializer, GalleryLikeCreateSerializer, \
    GalleryCommentListSerializer, GalleryCommentCreateSerializer

from .serializers import UserRegisterSerializer, UserSerializer, CustomJWTSerializer
import logging

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
        update_or_create_verification_token(profile, code, type='verify')
        logger.info(f'Код верификации емейла для пользователя {request.user} сохранен')
        if not task_send_email_to_user(profile.email, code):
            logger.info(f'Емейл для пользователя {request.user} не был отправлен')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'E-mail не был найден'})
        logger.info(f'Емейл для пользователя {request.user} был успешно отправлен')
        return Response(status=status.HTTP_200_OK, data={"message": 'Код успешно отправлен вам на E-mail'})

    def verify_email(self, request):
        """
        Функция получает код post запросом и токен пользователя
        Сравнивает полученный код и код записанный в таблице VerificationCode и возвращает статус 200
        если коды совпадают и статус 400 - если коды не совпали
        """
        logger.info(f'Пользователь {request.user} вводит код для подтвеждения емейла ')
        try:
            code = request.data['code']
            if check_email_verification_code(code):
                logger.info(f'Пользователь {request.user} успешно подтвердил почту ')
                return Response(status=status.HTTP_200_OK, data={"message": 'Ваш email успешно верефицирован'})
            logger.info(f'Пользователь {request.user} не подтвердил почту ')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":
                                                                      'Введенный код неверный. Попробуйте еще раз'})
        except KeyError:
            logger.error(f'Код не был передан')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "email или код не были переданы"})
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
        try:
            ip = get_ip(request)
            logger.info(f'Обновление пароля для пользователя {ip}')
            user = return_user_use_reset_token(request.data.get('token'))
            serializer = ChangePasswordSerializer(data=request.data, context={'user': user})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(f'Пароль для пользователя {ip} был сохранен')
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f'Пароль для пользователя {ip} не был изменен')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Ваш пароль не был изменен. '
                                                                                 'Пожалуйства обратитесь в поддержку'})
        except KeyError:
            logger.error(f'Не были передано нужные параметры')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Токен не был передан'})

    def generate_token_for_reset_password(self, request):
        """
        Функция восстановления пароля. После отправки запроса
        генерируется новый рандомный пароль и присваиватся юзеру
        с указанным логином. Данный код отсылается на указанную почту
        """
        try:
            username = request.data['username']
            logger.info(f'Отправка токена для восстановление пароля для пользователя {username} по емейл ')
            profile = Profile.objects.get(user__username=username)
            token = create_random_code(30)
            update_or_create_verification_token(profile, token, 'reset')
            if task_send_reset_password_to_email(profile.email, token):
                logger.info(f'Токен для пользователя {username} был успешно отправлен на емейл')
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Ссылка с восстановлением пароля '
                                                                                     'успешно отправлена '})
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Токен не был отправлен. '
                                                                                 'Пожалуйства обратитесь в поддержку'})
        except KeyError:
            logger.error(f'Не были передано нужные параметры')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Email не был переданы'})
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
        instance = Specialization.objects.all()
        logger.info(f'Для пользователя {ip} был получен список профи категорий')
        serializer = SpecializationListSerializer(instance, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_pro_categories(self, request):
        """
        Список специализаий фотографов и моделей
        """
        ip = get_ip(request)
        instance = ProCategory.objects.all()
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
            serializer = ProfilePublicSerializer(instance)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Профиль не был найден.'})

    def partial_update(self, request):
        """
        Частитичное или полное обновление полей в таблицу Profile
        """
        try:
            user = request.user
            check_is_unique_email(request.data['email'], user)
            instance = Profile.objects.get(user=user)
            logger.info(f'Обновление профиля для пользователя {user} было запрошено')
            serializer = ProfileUpdateSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(f'Обновление профиля для пользователя {user} был выполнено')
                return Response(status=status.HTTP_200_OK, data={"message": 'Обнввление профиля прошло успешно'})
            logger.error(f'Обновление профиля для пользователя {user} не было завершено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Обновление не было выполнено '
                                                                                 'Пожалуйства обратитесь в поддержку'})
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Не был передан email. '
                                                                                 'Пожалуйства обратитесь в поддержку'})

    def search_profiles(self, request):
        """
        Частитичное или полное обновление полей в таблицу Profile
        """
        try:
            ip = get_ip(request)
            filter_queryset = filter_by_all_parameters(request.GET)
            paginates_queryset = custom_paginator(filter_queryset, request)
            logger.info(f'Пользователь {ip} хочет найти профили')
            serializer = ProfileUpdateSerializer(paginates_queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Не был передан email. '
                                                                                 'Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class AlbumViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_album': [permissions.IsAuthenticated, ],
        }

    def create_album(self, request):
        logger.info(f'Пользователь {request.user} хочет создать альбом')
        profile = Profile.objects.get(user=request.user)
        serializer = AlbumCreateSerializer(data=request.data | {"profile": profile.id})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно создал альбом')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не смог добавить новый альбом')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Создание альбома не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def list_user_albums(self, request, pk):
        albums = Album.objects.filter(profile=pk)
        serializer = AlbumListSerializer(albums, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_album_photos(self, request, pk):
        albums = Gallery.objects.filter(album=pk)
        serializer = GalleryForCardListSerializer(albums, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_photo': [permissions.IsAuthenticated, ],
    }

    def create_photo(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить фото')
        profile = Profile.objects.get(user=request.user)
        serializer = GalleryCreateSerializer(data=request.data | {"profile": profile.id})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно создал фото')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не смог добавить фото')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Создание фото не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def retrieve_photo(self, request, pk):
        try:
            user_ip = get_ip(request)
            instance = Gallery.objects.get(id=pk)
            if protection_cheating_views(instance, user_ip):
                add_view(instance)
            serializer = GalleryListSerializer(instance)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото из галерии не было найдено'})

    def list_photos(self, request, pk):
        albums = Gallery.objects.filter(profile=pk)
        serializer = GalleryForCardListSerializer(albums, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated, ],
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет получить список избранных фото')
        queryset = GalleryFavorite.objects.filter(profile__user=request.user).select_related()
        serializer = GalleryFavoriteListSerializer(queryset, many=True)
        logger.info(f'Пользователь {request.user} успешно получил список избранных фото')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить фото в избранное')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_favorite(request.data.get('gallery'), profile):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такая фото уже есть в избранном'})
        serializer = GalleryFavoriteCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} учпешно добавил фото в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил фото в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет удалить фото из избранного')
            profile = Profile.objects.get(user=request.user)
            instance = GalleryFavorite.objects.get(profile=profile.id, gallery=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно удалил фото из избранного')
            return Response(status=status.HTTP_200_OK)
        except GalleryFavorite.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено избранное фото при удалении')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Избранное фото не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryLikeViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_like': [permissions.IsAuthenticated, ],
        'delete_like': [permissions.IsAuthenticated, ],
    }

    def create_like(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить лайк к фото')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_like(request.data.get('gallery'), profile):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такой лайк на фото уже есть'})
        serializer = GalleryLikeCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил лайк к фото')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил лайк к фото')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет убрать лайк')
            profile = Profile.objects.get(user=request.user)
            instance = GalleryLike.objects.filter(profile=profile, gallery=pk).first()
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно убрал лайк с фото')
            return Response(status=status.HTTP_200_OK)
        except GalleryLike.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено фото при удалении лайка')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryCommentViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'list_comments': [permissions.IsAuthenticated, ],
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_comments(self, request, pk):
        logger.info(f'Пользователь {request.user} хочет получить список комментариев')
        queryset = GalleryComment.objects.filter(gallery=pk).select_related()
        serializer = GalleryCommentListSerializer(queryset, many=True)
        logger.info(f'Пользователь {request.user} успешно получил список комментариев')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        profile = Profile.objects.get(user=request.user).id
        serializer = GalleryCommentCreateSerializer(data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил комментарий к фото')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил комментарий к фото')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]