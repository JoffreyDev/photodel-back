from rest_framework import serializers
from film_places.models import CategoryFilmPlaces, FilmPlaces, FilmPlacesFavorite, FilmPlacesComment, FilmPlacesLike
from services.film_places_service import check_unique_film_places
from accounts.api.serializers import ProfilePublicSerializer


class CategoryFilmPlacesListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание записи о месте съемки
    """
    class Meta:
        model = CategoryFilmPlaces
        fields = ['name_category', ]


class FilmPlacesCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание записи о месте съемки
    """
    class Meta:
        model = FilmPlaces
        fields = ['name_place', 'description', 'photo_camera',
                  'cost', 'payment', 'place_location', 'category', 'profile', 'rel_object', ]

    def validate(self, data):
        place = check_unique_film_places(data['place_location'])
        if place:
            data['rel_object'] = place
        return data


class FilmPlacesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlaces
        fields = ['name_place', 'description', 'photo_camera', 'place_image', 'views',
                  'cost', 'payment', 'place_location', 'category', 'profile', 'rel_object', ]


class FilmPlacesFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlacesFavorite
        fields = '__all__'


class FilmPlacesFavoriteListSerializer(serializers.ModelSerializer):
    profile = ProfilePublicSerializer()
    place = FilmPlacesListSerializer()

    class Meta:
        model = FilmPlacesFavorite
        fields = ['profile', 'place', ]


class FilmPlacesLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlacesLike
        fields = '__all__'


class FilmPlacesCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlacesComment
        fields = '__all__'


class FilmPlacesCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfilePublicSerializer()
    place = FilmPlacesListSerializer()

    class Meta:
        model = FilmPlacesComment
        fields = ['content', 'timestamp', 'sender_comment', 'place', ]

