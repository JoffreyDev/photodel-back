from rest_framework_simplejwt.serializers import TokenObtainSerializer
from django.contrib.auth.models import User, AnonymousUser
from rest_framework import serializers
from accounts.models import Profile, ProCategory, Specialization, \
    Album, Gallery, GalleryComment, GalleryLike, GalleryFavorite, GalleryImage
from services.film_places_service import ImageBase64Field, Base64ImageField
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import password_validation
from django.contrib.auth.models import update_last_login
from additional_entities.api.serializers import CountryListSerializer, LanguageListSerializer
import json


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


class CustomJWTSerializer(TokenObtainSerializer):
    """
    Сериализатор для кастомной авторизации пользователя
    """
    username = serializers.CharField(max_length=50, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if not qs.exists():
            raise serializers.ValidationError("Такого логина не было найдено. Пожалуйста, попробуйте еще раз")
        return value

    def validate(self, validate_data):
        data = super().validate(validate_data)
        refresh = RefreshToken.for_user(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        update_last_login(None, self.user)

        return data


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
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if self.context['user'] is AnonymousUser:
            raise serializers.ValidationError('Пользователь с таким логином не найден')
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError('Пароя не совпадают')
        password_validation.validate_password(data['new_password1'], self.context['user'])
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['user']
        user.set_password(password)
        user.save()
        return user


class GalleryImageSerializer(serializers.ModelSerializer):
    photo = ImageBase64Field()

    class Meta:
        model = GalleryImage
        fields = ['photo', ]


class SpecializationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name_spec', ]


class ProCategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProCategory
        fields = ['id', 'name_category', ]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'filming_geo', 'work_condition', 'cost_services', 'string_location_now',
                  'photo_technics', 'languages', 'about', 'status', 'type_pro', 'string_location',
                  'location', 'phone', 'site', 'email', 'instagram', 'facebook', 'vk',
                  'location_now', 'date_stay_start', 'date_stay_end', 'message', 'is_show_nu_photo',
                  'is_adult', 'avatar', 'spec_model_or_photographer', ]


class ProfilePublicSerializer(serializers.ModelSerializer):
    avatar = ImageBase64Field()
    filming_geo = CountryListSerializer(read_only=True, many=True)
    languages = LanguageListSerializer(read_only=True, many=True)
    spec_model_or_photographer = SpecializationListSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'filming_geo', 'work_condition', 'cost_services', 'string_location_now',
                  'photo_technics', 'languages', 'about', 'status', 'type_pro', 'string_location',
                  'location', 'phone', 'site', 'email', 'instagram', 'facebook', 'vk', 'avatar',
                  'location_now', 'date_stay_start', 'date_stay_end', 'message', 'is_adult',
                  'spec_model_or_photographer', ]


class ProfilePrivateSerializer(serializers.ModelSerializer):
    filming_geo = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    spec_model_or_photographer = serializers.SerializerMethodField()
    type_pro = serializers.SerializerMethodField()
    avatar = ImageBase64Field()

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'filming_geo', 'work_condition', 'cost_services', 'string_location_now',
                  'photo_technics', 'languages', 'about', 'status', 'type_pro', 'string_location',
                  'location', 'phone', 'site', 'email', 'instagram', 'facebook', 'vk', 'avatar',
                  'location_now', 'date_stay_start', 'date_stay_end', 'message', 'is_show_nu_photo', 'is_adult',
                  'spec_model_or_photographer', ]

    def get_spec_model_or_photographer(self, obj):
        return json.dumps([{i.id: i.name_spec} for i in obj.spec_model_or_photographer.all()])

    def get_filming_geo(self, obj):
        return json.dumps([{i.id: i.name_country} for i in obj.filming_geo.all()])

    def get_languages(self, obj):
        return json.dumps([{i.id: i.name_language} for i in obj.languages.all()])

    def get_type_pro(self, obj):
        if not obj.type_pro:
            return []
        return json.dumps([{obj.type_pro.id: obj.type_pro.name_category}])


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name_album', 'description_album', ]


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class GalleryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryForCardListSerializer(serializers.ModelSerializer):
    gallery_image = GalleryImageSerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['gallery_image', 'id', 'views', 'likes', 'comments', 'favorites', ]

    def get_likes(self, obj):
        return GalleryLike.objects.filter(gallery=obj.id).count()

    def get_comments(self, obj):
        return GalleryComment.objects.filter(gallery=obj.id).count()

    def get_favorites(self, obj):
        return GalleryFavorite.objects.filter(gallery=obj.id).count()


class GalleryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['gallery_image', 'name_image', 'description', 'place_location',
                  'photo_camera', 'focal_len', 'excerpt', 'flash', 'views', ]


class GalleryFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryFavorite
        fields = '__all__'


class GalleryFavoriteListSerializer(serializers.ModelSerializer):
    profile = ProfilePublicSerializer()
    gallery = GalleryForCardListSerializer()

    class Meta:
        model = GalleryFavorite
        fields = ['profile', 'gallery', ]


class GalleryLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryLike
        fields = '__all__'


class GalleryCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryComment
        fields = '__all__'


class GalleryCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfilePublicSerializer()
    gallery = GalleryForCardListSerializer()

    class Meta:
        model = GalleryComment
        fields = ['content', 'timestamp', 'sender_comment', 'gallery', ]
