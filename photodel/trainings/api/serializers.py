from rest_framework import serializers
from trainings.models import TrainingCategory, Trainings, TrainingsFavorite, \
    TrainingsComment, TrainingsLike, TrainingsRequest
from accounts.api.serializers import ProfileForGallerySerializer, ProfileWithAdditionalInfoSerializer
from gallery.api.serializers import ImageSerializer
from services.gallery_service import diff_between_two_points
from services.accounts_service import check_obscene_word_in_content
from django.contrib.auth.models import AnonymousUser


class CategoryTrainingsListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание записи о месте съемки
    """
    class Meta:
        model = TrainingCategory
        fields = ['id', 'name_category', ]


class TrainingsUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание записи об обучении
    """
    class Meta:
        model = Trainings
        fields = ['training_title', 'training_images', 'training_description', 'summary_members', 'reserved_places',
                  'place', 'place_location', 'string_place_location', 'start_date', 'end_date', 'views', 'is_hidden', 'profile', 'training_orgs', 'training_team', 'training_members', 'training_category', ]

    def validate(self, data):
        profile = self.context['profile']
        training_user = Trainings.objects.filter(profile=profile)
        if training_user.filter(training_name=data.get('training_name')).all().count() > 1:
            raise serializers.ValidationError(
                {'error': 'Обучение с таким названием уже существует'})
        return data


class TrainingsCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание записи о месте съемки
    """
    class Meta:
        model = Trainings
        fields = ['training_title', 'training_description', 'summary_members', 'training_images', 'place',
                  'place_location', 'string_place_location', 'start_date', 'end_date', 'main_photo', 'profile', 'training_team', 'training_orgs', 'training_category', 'cost', 'first_payment']

    def validate(self, data):
        profile = self.context['profile']
        user_training = Trainings.objects.filter(profile=profile)
        if user_training.filter(training_title=data.get('training_title')):
            raise serializers.ValidationError(
                {'error': 'Обучение с таким названием уже существует'})
        profile = self.context['profile']
        user_trainings = Trainings.objects.filter(profile=profile)
        if profile.pro_account == 0:
            raise serializers.ValidationError({'error': 'Чтобы добавить обучение, '
                                                        'пожалуйста, обновите Ваш пакет до Стандарт'})
        if profile.pro_account == 1 and user_trainings.count() >= 1:
            raise serializers.ValidationError({'error': 'Вы сможете добавить обучение через месяц. '
                                                        'Чтобы снять ограничения, пожалуйста, обновите Ваш пакет до Максимум'})
        return data


class TrainingsForCardSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    main_photo = ImageSerializer()
    profile = ProfileForGallerySerializer()
    reserved_places = serializers.SerializerMethodField()
    training_orgs = ProfileForGallerySerializer(read_only=True, many=True)

    class Meta:
        model = Trainings
        fields = ['id', 'training_title', 'main_photo', 'start_date', 'end_date',
                  'cost', 'place', 'likes', 'summary_members', 'reserved_places', 'favorites', 'comments', 'profile', 'string_place_location', 'training_orgs']

    def get_likes(self, obj):
        return TrainingsLike.objects.filter(training=obj.id).count()

    def get_comments(self, obj):
        return TrainingsComment.objects.filter(training=obj.id).count()

    def get_favorites(self, obj):
        return TrainingsFavorite.objects.filter(training=obj.id).count()

    def get_reserved_places(self, obj):
        return Trainings.objects.get(pk=obj.id).training_members.all().count()


class TrainingsListSerializer(serializers.ModelSerializer):
    profile = ProfileForGallerySerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    main_photo = ImageSerializer()
    training_orgs = ProfileForGallerySerializer(read_only=True, many=True)
    reserved_places = serializers.SerializerMethodField()

    class Meta:
        model = Trainings
        fields = ['id', 'training_title', 'main_photo', 'start_date', 'end_date',
                  'cost', 'likes', 'summary_members', 'reserved_places', 'profile', 'string_place_location', 'views', 'training_images', 'was_added', 'first_payment', 'place_location', 'training_category', 'training_description', 'comments', 'favorites', 'training_orgs', ]

    def get_likes(self, obj):
        return TrainingsLike.objects.filter(training=obj.id).count()

    def get_comments(self, obj):
        return TrainingsComment.objects.filter(training=obj.id).count()

    def get_favorites(self, obj):
        return TrainingsFavorite.objects.filter(training=obj.id).count()

    def get_reserved_places(self, obj):
        return Trainings.objects.get(pk=obj.id).training_members.all().count()


class TrainingsRetrieveSerializer(serializers.ModelSerializer):
    training_images = ImageSerializer(read_only=True, many=True)
    profile = ProfileForGallerySerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    in_favorite = serializers.SerializerMethodField()
    training_category = CategoryTrainingsListSerializer(read_only=True)
    training_team = ProfileForGallerySerializer(read_only=True, many=True)
    training_orgs = ProfileForGallerySerializer(read_only=True, many=True)
    training_members = ProfileForGallerySerializer(read_only=True, many=True)
    reserved_places = serializers.SerializerMethodField()

    class Meta:
        model = Trainings
        fields = ['id', 'training_title', 'main_photo', 'start_date', 'end_date',
                  'cost', 'place', 'likes', 'summary_members', 'reserved_places', 'favorites', 'comments', 'profile', 'string_place_location', 'views', 'is_liked', 'in_favorite', 'training_images', 'was_added', 'first_payment', 'place_location', 'training_category', 'training_description', 'training_team', 'training_members', 'training_orgs', ]

    def get_likes(self, obj):
        return TrainingsLike.objects.filter(training=obj.id).count()

    def get_comments(self, obj):
        return TrainingsComment.objects.filter(training=obj.id).count()

    def get_favorites(self, obj):
        return TrainingsFavorite.objects.filter(training=obj.id).count()

    def get_is_liked(self, obj):
        if isinstance(self.context.get('user', ''), AnonymousUser):
            return ''
        return bool(TrainingsLike.objects.filter(training=obj.id, profile__user=self.context['user']))

    def get_in_favorite(self, obj):
        if isinstance(self.context.get('user', ''), AnonymousUser):
            return ''
        return bool(TrainingsFavorite.objects.filter(training=obj.id, profile__user=self.context['user']))

    def get_reserved_places(self, obj):
        return Trainings.objects.get(pk=obj.id).training_members.all().count()


class TrainingsAllListSerializer(serializers.ModelSerializer):
    profile = ProfileForGallerySerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    main_photo = ImageSerializer()
    diff_distance = serializers.SerializerMethodField()
    training_orgs = ProfileForGallerySerializer(read_only=True, many=True)
    reserved_places = serializers.SerializerMethodField()

    class Meta:
        model = Trainings
        fields = ['id', 'training_title', 'main_photo', 'start_date', 'end_date',
                  'cost', 'place', 'likes', 'summary_members', 'reserved_places', 'favorites', 'comments', 'profile', 'diff_distance', 'string_place_location', 'training_orgs']

    def get_likes(self, obj):
        return TrainingsLike.objects.filter(training=obj.id).count()

    def get_comments(self, obj):
        return TrainingsComment.objects.filter(training=obj.id).count()

    def get_favorites(self, obj):
        return TrainingsFavorite.objects.filter(training=obj.id).count()

    def get_diff_distance(self, data):
        return diff_between_two_points(self.context.get('user_coords'), data.place_location)

    def get_reserved_places(self, obj):
        return Trainings.objects.get(pk=obj.id).training_members.all().count()


class TrainingsAllLisForMaptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainings
        fields = ['id', 'place_location', ]


class TrainingsFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingsFavorite
        fields = '__all__'


class TrainingsFavoriteListSerializer(serializers.ModelSerializer):
    profile = ProfileWithAdditionalInfoSerializer()
    training = TrainingsListSerializer()
    diff_distance = serializers.SerializerMethodField()

    class Meta:
        model = TrainingsFavorite
        fields = ['profile', 'training', 'id', 'diff_distance', ]

    def get_diff_distance(self, data):
        return diff_between_two_points(self.context.get('user_coords'), data.training.place_location)


class TrainingsLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingsLike
        fields = '__all__'


class TrainingsCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingsComment
        fields = '__all__'

    def validate(self, data):
        content = data.get('content', '').split()
        if check_obscene_word_in_content(content):
            raise serializers.ValidationError(
                {'error': 'Ваш комментарий содержит недопустимые слова'})
        comment = data.get('answer_id_comment')
        if not comment:
            return data
        if comment.answer_id_comment:
            raise serializers.ValidationError(
                {'error': 'Вы не можете ответить на ответ другого пользователя'})
        return data


class TrainingsCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfileForGallerySerializer()
    training = TrainingsListSerializer()

    class Meta:
        model = TrainingsComment
        fields = ['content', 'timestamp',
                  'sender_comment', 'training', 'id', 'quote_id', ]


class TrainingCreateRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingsRequest
        fields = '__all__'

    def validate(self, data):
        sender = data.get('request_user')
        training = data.get('training')
        if sender.id == training.profile.id:
            raise serializers.ValidationError(
                {'error': 'Нельзя записаться в свое обучение!'})
        training_team = training.training_team.all()
        if sender in training_team:
            raise serializers.ValidationError(
                {'error': 'Нельзя записаться в обучение, так как вы в команде обучения!'})
        training_orgs = training.training_orgs.all()
        if sender in training_orgs:
            raise serializers.ValidationError(
                {'error': 'Нельзя записаться в обучение, так как вы - организатор обучения!'})
        user_requests = TrainingsRequest.objects.filter(request_user=sender)
        simmilar_requests = user_requests.filter(training_id=training.id)
        if simmilar_requests.filter(status='AWAITING'):
            raise serializers.ValidationError(
                {'error': 'Уже есть запрос, который ожидает рассмотрения'})
        if simmilar_requests.filter(status='ACCEPTED'):
            raise serializers.ValidationError(
                {'error': 'Вы уже записаны на это обучение!'})
        if training.training_members.all().count() >= training.summary_members:
            raise serializers.ValidationError(
                {'error': 'Все места уже забронированы!'})
        return data


class TrainingRequestSerializer(serializers.ModelSerializer):

    training_images = ImageSerializer(read_only=True, many=True)
    profile = ProfileForGallerySerializer()

    class Meta:
        model = Trainings
        fields = ['training_title', 'start_date',
                  'end_date', 'training_images', 'profile']


class TrainingsInvitesList(serializers.ModelSerializer):
    request_user = ProfileForGallerySerializer()
    training = TrainingRequestSerializer()

    class Meta:
        model = TrainingsRequest
        fields = ['request_user', 'status', 'id', 'training']


class TrainingRequestChangeSerializer(serializers.ModelSerializer):

    request_id = serializers.IntegerField()
    status = serializers.ChoiceField(
        choices=TrainingsRequest.STATUS_CHOICES)

    class Meta:
        model = TrainingsRequest
        fields = ['request_id', 'status']

    def validate_request_id(self, request_id):
        invite = TrainingsRequest.objects.filter(id=request_id).exists()
        if not invite:
            raise serializers.ValidationError(
                {'error': 'Приглашение не найдено'})
        return request_id
