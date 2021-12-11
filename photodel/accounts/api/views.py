from rest_framework import generics, permissions, status, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from accounts.models import Profile, VerificationCode
from rest_framework_simplejwt.views import TokenViewBase
from services.accounts_service import check_email_verification_code, update_or_create_verification_code, \
    change_user_password, create_random_code, check_is_unique_email

from tasks.accounts_task import task_send_email_to_user, task_send_reset_password_to_email
from .serializers import ProfileUpdateSerializer, ChangePasswordSerializer

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
        update_or_create_verification_code(profile, code)
        logger.info(f'Код верификации емейла для пользователя {request.user} сохранен')
        if not task_send_email_to_user(profile.email, code):
            logger.info(f'Емейл для пользователя {request.user} не был отправлен')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='E-mail не был найден')
        logger.info(f'Емейл для пользователя {request.user} был успешно отправлен')
        return Response(status=status.HTTP_200_OK, data='Код успешно отправлен вам на E-mail')

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
                return Response(status=status.HTTP_200_OK, data='Ваш email успешно верефицирован')
            logger.info(f'Пользователь {request.user} не подтвердил почту ')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Введенный код неверный. Попробуйте еще раз')
        except KeyError:
            logger.error(f'Код не был передан')
            return Response(status=status.HTTP_400_BAD_REQUEST, data="email или код не были переданы")
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Пользователь не был найден")

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ChangePasswordView(viewsets.ViewSet):
    permission_classes_by_action = {
        'update_password': [permissions.IsAuthenticated, ],
        }

    def update_password(self, request, *args, **kwargs):
        """
        Обновление пароля для авторизированного юзера
        """
        logger.info(f'Обновление пароля для пользователя {request.user}')
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пароль для пользователя {request.user} был сохранен')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пароль для пользователя {request.user} не был изменен')
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Ваш пароль не был изменен. '
                                                                 'Пожалуйства обратитесь в поддержку')

    def set_generate_password_use_email(self, request):
        """
        Функция восстановления пароля. После отправки запроса
        генерируется новый рандомный пароль и присваиватся юзеру
        с указанным логином. Данный код отсылается на указанную почту
        """
        try:
            username = request.data['username']
            logger.info(f'Восстановление пароля для пользователя {username} по емейл ')
            profile = Profile.objects.get(user__username=username)
            random_password = generate_random_password(8)
            if task_send_reset_password_to_email(profile.email, random_password):
                logger.info(f'Пароль для пользователя {username} был успешно отправлен на емейл')
                if change_user_password(profile.user.id, random_password):
                    return Response(status=status.HTTP_200_OK, data='Новый пароль был успешно отправлен на email')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Пароль не был отправлен '
                                                                     'Пожалуйства обратитесь в поддержку')
        except KeyError:
            logger.error(f'Не были передано нужные параметры')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Email или логин не были переданы')
        except Profile.DoesNotExist:
            logger.error(f'Пользователь не был найден')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Пользовтаель не был найден')

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ProfileViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'partial_update': [permissions.IsAuthenticated, ],
        }

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
                return Response(status=status.HTTP_200_OK, data='Обнввление профиля прошло успешно')
            logger.error(f'Обновление профиля для пользователя {user} не было завершено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Обновление не было выполнено '
                                                                     'Пожалуйства обратитесь в поддержку')
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Не был передан email. '
                                                                     'Пожалуйства обратитесь в поддержку')

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
