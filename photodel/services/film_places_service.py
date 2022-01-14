from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from film_places.models import CategoryFilmPlaces, FilmPlaces, FilmPlacesFavorite
from additional_entities.models import CustomSettings
from rest_framework import serializers
from django.conf import settings
from PIL import Image
from PIL import UnidentifiedImageError
import base64
import io
from django.core.files.base import ContentFile
import uuid
import six


class ImageBase64Field(serializers.ImageField):
    """
    Класс преобразования картинки в base64 строку
    """
    def to_representation(self, obj):
        """
        Функция преобразования картинки в base64
        """
        try:
            with open(str(settings.BASE_DIR) + obj.url, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode('utf-8')
        except ValueError:
            return None
        except FileNotFoundError:
            return None


class Base64ImageField(serializers.ImageField):
    """
    Класс сериализации base64 в изображение
    """

    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension


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
