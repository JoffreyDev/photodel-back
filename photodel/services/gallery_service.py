from gallery.models import GalleryFavorite, GalleryLike, AlbumLike, AlbumFavorite,\
    PhotoSessionLike, PhotoSessionFavorite
from film_places.models import FilmPlacesLike, FilmPlacesFavorite
from accounts.models import ProfileLike, ProfileFavorite
from services.accounts_service import convert_string_coordinates_to_point_obj

from rest_framework import serializers
from django.conf import settings
import base64
from django.core.files.base import ContentFile
import uuid
import six
import math


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


def is_unique_favorite(obj_id, profile_id, model):
    """
    Проверка на уникальность избранного
    """
    if model == 'gallery' and GalleryFavorite.objects.filter(gallery=obj_id, profile=profile_id):
        return False
    if model == 'profile' and ProfileFavorite.objects.filter(receiver_favorite=obj_id, sender_favorite=profile_id):
        return False
    if model == 'places' and FilmPlacesFavorite.objects.filter(place=obj_id, profile=profile_id):
        return False
    if model == 'album' and AlbumFavorite.objects.filter(album=obj_id, profile=profile_id):
        return False
    if model == 'photo_session' and PhotoSessionFavorite.objects.filter(photo_session=obj_id, profile=profile_id):
        return False
    return True


def is_unique_like(obj_id, profile_id, model):
    """
    Проверка на уникальность лайка
    """
    if model == 'gallery' and GalleryLike.objects.filter(gallery=obj_id, profile=profile_id):
        return False
    if model == 'profile' and ProfileLike.objects.filter(receiver_like=obj_id, sender_like=profile_id):
        return False
    if model == 'places' and FilmPlacesLike.objects.filter(place=obj_id, profile=profile_id):
        return False
    if model == 'album' and AlbumLike.objects.filter(album=obj_id, profile=profile_id):
        return False
    if model == 'photo_session' and PhotoSessionLike.objects.filter(photo_session=obj_id, profile=profile_id):
        return False
    return True


def protection_cheating_views(instance, ip):
    """
    Защита от накрутки просмотров вещи, путем
    сравнивания последннего ip адреса фото,
    которую просмотрел пользователь
    """
    if instance.last_ip_user != ip:
        instance.last_ip_user = ip
        instance.save()
        return True
    return False


def add_view(instance):
    """
    Функция добавления просмотра
    """
    instance.views += 1
    instance.save()


def diff_between_two_points(user_coordinates, field_with_location):
    """
    Расчет расстояние между двумя Point обьектами
    Перевод расстояния в киллометры и округление в большую сторону
    """
    if not user_coordinates or not field_with_location:
        return ''
    diff = field_with_location.distance(convert_string_coordinates_to_point_obj(user_coordinates)) * 100
    return f'{math.ceil(diff)}км'
