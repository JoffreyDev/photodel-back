from rest_framework import permissions
from accounts.models import Profile
from gallery.models import Image, Album, Gallery
from rest_framework.permissions import SAFE_METHODS


class IsOwnerImage(permissions.BasePermission):
    """
    Проверка на принадлежность фотки обложки альбома тому же юзеру, который создает альбом
    """
    message = {"error": "Вы не можете в обложку альбома добавить не свою фотографию"}

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.data.get('main_photo_id'):
            image = Image.objects.filter(id=request.data.get('main_photo_id')).first()
            return image.profile.user == request.user
        return True


class IsAddOrDeletePhotoFromAlbum(permissions.BasePermission):
    """
    Проверка на принадлежность фотки и альбома юзеру, который хочет удалить или добавить фотку в альбом
    """
    message = {"error": "Вы не можете удалить или добавить чужую фотографию с альбома"}

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            album_id = request.data.get('album_id')
            photos_id = request.data.get('photos_id')
            if album_id and photos_id:
                album = Album.objects.get(id=album_id)
                photos = Gallery.objects.filter(id__in=photos_id, profile__user=request.user).count()
                return request.user == album.profile.user and photos == len(photos_id)
            return True
        except Album.DoesNotExist:
            return False


class IsCreatePhoto(permissions.BasePermission):
    """
    Проверка на принадлежность альбома и фотки юезру который создает фотку в галерее
    """
    message = {"error": "Вы не можете создать фото в галерее, альбом или фото не являеются вашими"}

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            album = request.data.get('album')
            gallery_image = request.data.get('gallery_image')
            if gallery_image and Image.objects.get(id=gallery_image).profile.user != request.user:
                return False
            if album and Album.objects.filter(id__in=album, profile__user=request.user).count() != len(album):
                return False
            return True
        except Album.DoesNotExist:
            return False
        except Gallery.DoesNotExist:
            return False


class IsDeleteAlbum(permissions.BasePermission):
    """
    Проверка на удаление альбома
    """
    message = {"error": "Вы не можете удалить альбом, альбом не являеется вашими"}

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            album = view.kwargs['pk']
            if album and Album.objects.get(id=album).profile.user != request.user:
                return False
            return True
        except Album.DoesNotExist:
            return False
