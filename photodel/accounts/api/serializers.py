from rest_framework_simplejwt.serializers import TokenObtainSerializer
from django.contrib.auth.models import User, AnonymousUser
from rest_framework import serializers
from accounts.models import Profile, VerificationCode, ProCategory, Specialization, \
    ProfileComment, ProfileLike, ProfileFavorite
from services.gallery_service import ImageBase64Field, Base64ImageField, diff_between_two_points
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import password_validation
from django.contrib.auth.models import update_last_login
from additional_entities.api.serializers import CountryListSerializer, LanguageListSerializer
from services.accounts_service import check_profile_location, collect_favorite, \
    collect_like, check_obscene_word_in_content, collect_comment
from services.statistics_profile_service import collect_profile_statistics
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
        profile = Profile.objects.get(user=self.user)
        if not profile.email_verify:
            raise serializers.ValidationError("Вы не можете войти, Ваша почта не пожтверждена")
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
                  'is_adult', 'avatar', 'spec_model_or_photographer', 'ready_status', 'is_change', ]

    def validate(self, data):
        """
        Проверка пользователя на тип профиля и специализацию.
        """
        content = data.get('about', '').split()
        if check_obscene_word_in_content(content):
            raise serializers.ValidationError({'error': 'В вашей информации содержиатся недопустимые слова'})
        type_pro = data.get('type_pro')
        spec = data.get('spec_model_or_photographer')
        if not type_pro and not spec:
            return data
        if not type_pro and spec:
            raise serializers.ValidationError({"error": 'Вы не можете указать специальность '
                                                        'без указаного типа профиля'})
        if (type_pro.name_category != 'Модели' and type_pro.name_category != 'Фотографы') and spec:
            raise serializers.ValidationError({"error": "Вы не являетесь моделью или "
                                                        "фотографом для выбора специализации"})
        return data


class ProfileForPublicSerializer(serializers.ModelSerializer):
    avatar = ImageBase64Field()
    filming_geo = CountryListSerializer(read_only=True, many=True)
    languages = LanguageListSerializer(read_only=True, many=True)
    spec_model_or_photographer = SpecializationListSerializer(read_only=True, many=True)
    type_pro = ProCategoryListSerializer()
    statistics = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'filming_geo', 'work_condition', 'cost_services', 'string_location_now',
                  'photo_technics', 'languages', 'about', 'status', 'type_pro', 'string_location',
                  'location', 'phone', 'site', 'email', 'instagram', 'facebook', 'vk', 'avatar',
                  'location_now', 'date_stay_start', 'date_stay_end', 'message', 'is_adult',
                  'spec_model_or_photographer', 'ready_status', 'statistics', 'user_channel_name',
                  'rating', 'date_register', ]

    def get_statistics(self, obj):
        return collect_profile_statistics(obj)


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
                  'spec_model_or_photographer', 'ready_status', ]


class ProfileForGallerySerializer(serializers.ModelSerializer):
    avatar = ImageBase64Field()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'surname', 'avatar', 'user_channel_name', 'rating', ]


class ProfileWithAdditionalInfoSerializer(serializers.ModelSerializer):
    avatar = ImageBase64Field()
    count_favorites = serializers.SerializerMethodField()
    count_likes = serializers.SerializerMethodField()
    count_comments = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'surname', 'user_channel_name', 'type_pro',
                  'spec_model_or_photographer', 'rating', 'avatar',
                  'location', 'string_location', 'location_now', 'string_location_now',
                  'count_favorites', 'count_likes', 'count_comments', ]

    def get_count_favorites(self, obj):
        return collect_favorite(obj.user)

    def get_count_likes(self, obj):
        return collect_like(obj.user)

    def get_count_comments(self, obj):
        return collect_comment(obj.user)


class ProfilePrivateSerializer(serializers.ModelSerializer):
    filming_geo = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    spec_model_or_photographer = serializers.SerializerMethodField()
    type_pro = serializers.SerializerMethodField()
    statistics = serializers.SerializerMethodField()
    avatar = ImageBase64Field()

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'filming_geo', 'work_condition', 'cost_services', 'string_location_now',
                  'photo_technics', 'languages', 'about', 'status', 'type_pro', 'string_location',
                  'location', 'phone', 'site', 'email', 'instagram', 'facebook', 'vk', 'avatar',
                  'location_now', 'date_stay_start', 'date_stay_end', 'message', 'is_show_nu_photo', 'is_adult',
                  'spec_model_or_photographer', 'ready_status', 'id', 'statistics', 'date_register',
                  'rating', 'is_change', ]

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

    def get_statistics(self, obj):
        return collect_profile_statistics(obj)


class ProfilListSerializer(serializers.ModelSerializer):
    avatar = ImageBase64Field()
    type_pro = ProCategoryListSerializer()
    spec_model_or_photographer = SpecializationListSerializer(read_only=True, many=True)
    diff_distance = serializers.SerializerMethodField()
    count_favorites = serializers.SerializerMethodField()
    count_likes = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'string_location_now', 'location_now', 'avatar',
                  'type_pro', 'string_location', 'location', 'diff_distance',
                  'spec_model_or_photographer', 'user_channel_name', 'count_favorites',
                  'count_likes', 'rating', ]

    def get_diff_distance(self, obj):
        location = check_profile_location(obj)
        return diff_between_two_points(self.context.get('user_coords'), location)

    def get_count_favorites(self, obj):
        return collect_favorite(obj.user)

    def get_count_likes(self, obj):
        return collect_like(obj.user)


class ProfileForFavoriteSerializer(serializers.ModelSerializer):
    avatar = ImageBase64Field()
    spec_model_or_photographer = SpecializationListSerializer(read_only=True, many=True)
    type_pro = ProCategoryListSerializer()
    count_favorites = serializers.SerializerMethodField()
    count_likes = serializers.SerializerMethodField()
    count_comments = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'surname', 'user_channel_name', 'type_pro',
                  'spec_model_or_photographer', 'rating', 'avatar',
                  'location', 'string_location', 'location_now', 'string_location_now',
                  'count_favorites', 'count_likes', 'count_comments', ]

    def get_count_favorites(self, obj):
        return collect_favorite(obj.user)

    def get_count_likes(self, obj):
        return collect_like(obj.user)

    def get_count_comments(self, obj):
        return collect_comment(obj.user)


class ProfileFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFavorite
        fields = '__all__'


class ProfileFavoriteListSerializer(serializers.ModelSerializer):
    receiver_favorite = ProfileForFavoriteSerializer()
    diff_distance = serializers.SerializerMethodField()

    class Meta:
        model = ProfileFavorite
        fields = ['sender_favorite', 'receiver_favorite', 'diff_distance', ]

    def get_diff_distance(self, obj):
        location = check_profile_location(obj.receiver_favorite)
        return diff_between_two_points(self.context.get('user_coords'), location)


class ProfileLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileLike
        fields = '__all__'


class ProfileCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileComment
        fields = '__all__'

    def validate(self, data):
        content = data.get('content', '').split()
        if check_obscene_word_in_content(content):
            raise serializers.ValidationError({'error': 'Ваш комментарий содержит недопустимые слова'})
        comment = data.get('answer_id_comment')
        if not comment:
            return data
        if comment.answer_id_comment:
            raise serializers.ValidationError({'error': 'Вы не можете ответить на ответ другого пользователя'})
        return data


class ProfileCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfilePublicSerializer()
    receiver_comment = ProfilePublicSerializer()

    class Meta:
        model = ProfileComment
        fields = ['content', 'timestamp', 'sender_comment', 'receiver_comment', 'answer_id_comment', 'quote_id', ]
