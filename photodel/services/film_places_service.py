from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Q
from geopy.distance import geodesic
from film_places.models import CategoryFilmPlaces, FilmPlaces, Favorite, Image
from additional_entities.models import CustomSettings


def convert_string_coordinates_to_point_obj(coordinates):
    """
    Функция конвертации координат в Point объект
    КоОрдинаты могут быть двух типов SRID=4326;POINT (27.449901 53.903557) и 27.449901 53.903557
    Если переданные координаты не кооректны для одно из типов, то возврващается координаты г.Москвы
    """
    try:
        split_coord = coordinates.split()
        if 'SRID' in coordinates:
            first, second = split_coord[1][1:], split_coord[2][:-1]
        else:
            first, second = split_coord[0], split_coord[1]
        pnt = Point(float(first), float(second))
        return pnt
    except Exception:
        return Point(55.753220, 37.622513)


def check_unique_film_places(place_coordinates):
    """
    Функция проверки уникальное ли место съемки.
    Если место уникально то возврваещется None
    Если место не уникально возвращается id место родителя
    Уникальное место зависит от параметры distance которое находится в настрйоках
    """
    all_places = FilmPlaces.objects.all()
    distance = CustomSettings.objects.all().first().distance_for_unique_places
    pnt = convert_string_coordinates_to_point_obj(place_coordinates)
    for _ in all_places:
        film = FilmPlaces.objects.filter(place_location__distance_lte=(pnt, D(m=distance)))
        if film:
            return film.last()
        return None
