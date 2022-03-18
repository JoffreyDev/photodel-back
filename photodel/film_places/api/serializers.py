from rest_framework import serializers
from film_places.models import CategoryFilmPlaces, FilmPlaces, FilmPlacesFavorite, \
    FilmPlacesComment, FilmPlacesLike, FilmRequest
from accounts.api.serializers import ProfileForGallerySerializer
from gallery.api.serializers import ImageSerializer
from services.gallery_service import diff_between_two_points


class CategoryFilmPlacesListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание записи о месте съемки
    """
    class Meta:
        model = CategoryFilmPlaces
        fields = ['name_category', 'id', ]


class FilmPlacesCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание записи о месте съемки
    """
    class Meta:
        model = FilmPlaces
        fields = ['name_place', 'description', 'photo_camera', 'place_image', 'string_place_location',
                  'cost', 'payment', 'place_location', 'category', 'profile', 'is_hidden', ]

    def validate(self, data):
        profile = self.context['profile']
        user_place = FilmPlaces.objects.filter(profile=profile, name_place=data.get('name_place'))
        if user_place:
            raise serializers.ValidationError({'error': 'Место съемки с таким названием уже существует'})
        return data


class FilmPlacesForCardSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = FilmPlaces
        fields = ['id', 'views', 'likes', 'comments', 'favorites', ]

    def get_likes(self, obj):
        return FilmPlacesLike.objects.filter(place=obj.id).count()

    def get_comments(self, obj):
        return FilmPlacesComment.objects.filter(place=obj.id).count()

    def get_favorites(self, obj):
        return FilmPlacesFavorite.objects.filter(place=obj.id).count()


class FilmPlacesBestSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = FilmPlaces
        fields = ['id', 'views', 'likes', ]

    def get_likes(self, obj):
        # FilmPlacesLike.objects.values('place').annotate(dcount=Count('place')).order_by('-dcount')
        return obj.id


class FilmPlacesListSerializer(serializers.ModelSerializer):
    place_image = ImageSerializer(read_only=True, many=True)
    category = CategoryFilmPlacesListSerializer(read_only=True, many=True)
    profile = ProfileForGallerySerializer()

    class Meta:
        model = FilmPlaces
        fields = ['id', 'name_place', 'description', 'photo_camera', 'place_image',
                  'views', 'string_place_location', 'cost', 'payment',
                  'place_location', 'category', 'profile', 'is_hidden', ]


class FilmPlacesAllListSerializer(serializers.ModelSerializer):
    place_image = ImageSerializer(read_only=True, many=True)
    profile = ProfileForGallerySerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    diff_distance = serializers.SerializerMethodField()

    class Meta:
        model = FilmPlaces
        fields = ['id', 'name_place', 'place_image', 'string_place_location',
                  'place_location', 'profile', 'likes', 'comments', 'favorites', 'diff_distance', 'last_views']

    def get_likes(self, obj):
        return FilmPlacesLike.objects.filter(place=obj.id).count()

    def get_comments(self, obj):
        return FilmPlacesComment.objects.filter(place=obj.id).count()

    def get_favorites(self, obj):
        return FilmPlacesFavorite.objects.filter(place=obj.id).count()

    def get_diff_distance(self, data):
        return diff_between_two_points(self.context.get('user_coords'), data.place_location)


class FilmPlacesFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlacesFavorite
        fields = '__all__'


class FilmPlacesFavoriteListSerializer(serializers.ModelSerializer):
    profile = ProfileForGallerySerializer()
    place = FilmPlacesListSerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    diff_distance = serializers.SerializerMethodField()

    class Meta:
        model = FilmPlacesFavorite
        fields = ['profile', 'place', 'likes', 'comments', 'favorites', 'id', 'diff_distance', ]

    def get_likes(self, obj):
        return FilmPlacesLike.objects.filter(place=obj.place.id).count()

    def get_comments(self, obj):
        return FilmPlacesComment.objects.filter(place=obj.place.id).count()

    def get_favorites(self, obj):
        return FilmPlacesFavorite.objects.filter(place=obj.place.id).count()

    def get_diff_distance(self, data):
        return diff_between_two_points(self.context.get('user_coords'), data.place.place_location)


class FilmPlacesLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlacesLike
        fields = '__all__'


class FilmPlacesCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlacesComment
        fields = '__all__'

    def validate(self, data):
        comment = data.get('answer_id_comment')
        if not comment:
            return data
        if comment.answer_id_comment:
            raise serializers.ValidationError({'error': 'Вы не можете ответить на ответ другого пользователя'})
        return data


class FilmPlacesCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfileForGallerySerializer()
    place = FilmPlacesListSerializer()

    class Meta:
        model = FilmPlacesComment
        fields = ['content', 'timestamp', 'sender_comment', 'place', 'id', ]


class FilmRequestCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmRequest
        fields = '__all__'

