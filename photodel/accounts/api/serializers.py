from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import password_validation


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'token': str(refresh.access_token),
    }


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализотор для авторизации юзера и выдачи access refresh токена
    """
    class Meta:
        model = User
        fields = ['username']


class CustomJWTSerializer(TokenObtainPairSerializer):
    """
    Сериализатор для кастомной авторизации пользователя
    """
    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if not qs.exists():
            raise serializers.ValidationError("Такого логина не было найдено. Пожалуйста, попробуйте еще раз")
        return value

    def validate(self, validate_data):
        credentials = {
            'username': '',
            'password': validate_data.get("password")
        }

        user_obj = User.objects.filter(username=validate_data.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username
        return super().validate(credentials)


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Сериализотор для регистраици юзера и выдачи access refresh токена
    """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'password2',
            'token',
        ]

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Пользователь с таким логином уже существует. Введите другой")
        return value

    def get_token(self, instance):
        token = get_tokens_for_user(instance).get("token")
        return token

    def create(self, validated_data):
        user_obj = User.objects.create(username=validated_data.get('username'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj


class ChangePasswordSerializer(serializers.Serializer):
    """
    Сериализотор для изменения пароля
    """
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                 'Ваш старый пароль введен неправильно. Пожалуйста, попробуйте еще раз'
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError('Пароя не совпадают')
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'filming_geo', 'work_condition', 'cost_services',
                  'photo_technics', 'languages', 'about', 'status', 'type_pro',
                  'location', 'phone', 'site', 'email', 'instagram', 'facebook', 'vk',
                  'location_now', 'date_stay_start', 'date_stay_end', 'message', 'is_show_nu_photo', 'is_adult', ]
