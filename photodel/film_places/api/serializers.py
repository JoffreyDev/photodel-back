from django.contrib.auth.models import User, AnonymousUser
from rest_framework import serializers
from film_places.models import FilmPlaces, CategoryFilmPlaces
from services.film_places_service import check_unique_film_places


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

