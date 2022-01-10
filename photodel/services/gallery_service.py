from gallery.models import GalleryFavorite, GalleryLike, AlbumLike, AlbumFavorite,\
    PhotoSessionLike, PhotoSessionFavorite
from film_places.models import FilmPlacesLike, FilmPlacesFavorite
from accounts.models import ProfileLike, ProfileFavorite


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
    if model == 'photo_session' and PhotoSessionLike.objects.filter(gallery=obj_id, profile=profile_id):
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
    if model == 'photo_session' and PhotoSessionFavorite.objects.filter(gallery=obj_id, profile=profile_id):
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