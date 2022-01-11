from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from gallery.models import Album, Gallery, Image, GalleryComment, GalleryLike, GalleryFavorite, \
    AlbumComment, AlbumLike, AlbumFavorite, PhotoSessionComment, PhotoSessionLike, \
    PhotoSessionFavorite, PhotoSession
from accounts.models import Profile
from services.gallery_service import is_unique_favorite, is_unique_like, \
    protection_cheating_views, add_view
from services.ip_service import get_ip
from .serializers import AlbumListSerializer, AlbumCreateSerializer, GalleryListSerializer, \
    GalleryForCardListSerializer, GalleryCreateSerializer, GalleryFavoriteCreateSerializer, \
    GalleryFavoriteListSerializer, GalleryLikeCreateSerializer, GalleryCommentListSerializer, \
    GalleryCommentCreateSerializer, PhotoSessionCreateSerializer, ImageSerializer, \
    AlbumFavoriteCreateSerializer, AlbumFavoriteListSerializer, AlbumLikeCreateSerializer, \
    AlbumCommentCreateSerializer, AlbumCommentListSerializer

import logging

logger = logging.getLogger(__name__)


class ImageViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_image': [permissions.IsAuthenticated, ],
        }

    def create_image(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ImageSerializer(data=request.data | {"profile": profile.id})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление изображение не было выполнено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class AlbumViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_album': [permissions.IsAuthenticated, ],
        'delete_photo_from_album': [permissions.IsAuthenticated, ],
        }

    def create_album(self, request):
        logger.info(f'Пользователь {request.user} хочет создать альбом')
        profile = Profile.objects.get(user=request.user)
        serializer = AlbumCreateSerializer(data=request.data | {"profile": profile.id}, context={'profile': profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно создал альбом')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не смог добавить новый альбом')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Создание альбома не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def list_user_albums(self, request, pk):
        albums = Album.objects.filter(profile=pk)
        serializer = AlbumListSerializer(albums, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_album_photos(self, request, pk):
        albums = Gallery.objects.filter(album=pk)
        serializer = GalleryForCardListSerializer(albums, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete_photo_from_album(self, request, album_id, photo_id):
        try:
            instance = Gallery.objects.get(id=photo_id)
            instance.album.remove(album_id)
            return Response(status=status.HTTP_200_OK)
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото из галерии не было найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class AlbumFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated, ],
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет получить список избранных альбомов')
        queryset = AlbumFavorite.objects.filter(profile__user=request.user).select_related()
        serializer = AlbumFavoriteListSerializer(queryset, many=True)
        logger.info(f'Пользователь {request.user} успешно получил список избранных альбомов')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить альбом в избранное')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_favorite(request.data.get('album'), profile, 'album'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такой альбом уже есть в избранном'})
        serializer = AlbumFavoriteCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил альбом в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил альбом в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет удалить альбом из избранного')
            profile = Profile.objects.get(user=request.user)
            instance = AlbumFavorite.objects.get(profile=profile.id, album=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно удалил альбом из избранного')
            return Response(status=status.HTTP_200_OK)
        except AlbumFavorite.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено избранный альбом при удалении')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Избранный альбом не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class AlbumLikeViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_like': [permissions.IsAuthenticated, ],
        'delete_like': [permissions.IsAuthenticated, ],
    }

    def create_like(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить лайк к альбому')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_like(request.data.get('album'), profile, 'album'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такой лайк на альбоме уже есть'})
        serializer = AlbumLikeCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил лайк к альбому')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил лайк к альбому')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет убрать лайк с альбома')
            profile = Profile.objects.get(user=request.user)
            instance = AlbumLike.objects.get(profile=profile, album=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно убрал лайк с альбома')
            return Response(status=status.HTTP_200_OK)
        except AlbumLike.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не был найден альбом при удалении лайка')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Альбом не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class AlbumCommentViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_comments(self, request, pk):
        queryset = AlbumComment.objects.filter(album=pk).select_related()
        serializer = AlbumCommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        profile = Profile.objects.get(user=request.user).id
        serializer = AlbumCommentCreateSerializer(data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил комментарий к альбому')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил комментарий к альбому')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_photo': [permissions.IsAuthenticated, ],
    }

    def create_photo(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить фото')
        profile = Profile.objects.get(user=request.user)
        serializer = GalleryCreateSerializer(data=request.data | {"profile": profile.id}, context={'profile': profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно создал фото')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не смог добавить фото')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Создание фото не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def retrieve_photo(self, request, pk):
        try:
            user_ip = get_ip(request)
            instance = Gallery.objects.get(id=pk)
            if protection_cheating_views(instance, user_ip):
                add_view(instance)
            serializer = GalleryListSerializer(instance)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото из галерии не было найдено'})

    def list_photos(self, request, pk):
        photos = Gallery.objects.filter(profile=pk)
        serializer = GalleryForCardListSerializer(photos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated, ],
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет получить список избранных фото')
        queryset = GalleryFavorite.objects.filter(profile__user=request.user).select_related()
        serializer = GalleryFavoriteListSerializer(queryset, many=True)
        logger.info(f'Пользователь {request.user} успешно получил список избранных фото')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить фото в избранное')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_favorite(request.data.get('gallery'), profile, 'gallery'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такая фото уже есть в избранном'})
        serializer = GalleryFavoriteCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} учпешно добавил фото в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил фото в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет удалить фото из избранного')
            profile = Profile.objects.get(user=request.user)
            instance = GalleryFavorite.objects.get(profile=profile.id, gallery=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно удалил фото из избранного')
            return Response(status=status.HTTP_200_OK)
        except GalleryFavorite.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено избранное фото при удалении')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Избранное фото не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryLikeViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_like': [permissions.IsAuthenticated, ],
        'delete_like': [permissions.IsAuthenticated, ],
    }

    def create_like(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить лайк к фото')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_like(request.data.get('gallery'), profile, 'gallery'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такой лайк на фото уже есть'})
        serializer = GalleryLikeCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил лайк к фото')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил лайк к фото')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет убрать лайк')
            profile = Profile.objects.get(user=request.user)
            instance = GalleryLike.objects.get(profile=profile, gallery=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно убрал лайк с фото')
            return Response(status=status.HTTP_200_OK)
        except GalleryLike.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено фото при удалении лайка')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryCommentViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_comments(self, request, pk):
        queryset = GalleryComment.objects.filter(gallery=pk).select_related()
        serializer = GalleryCommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        profile = Profile.objects.get(user=request.user).id
        serializer = GalleryCommentCreateSerializer(data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил комментарий к фото')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил комментарий к фото')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class PhotoSessionViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_photo_session': [permissions.IsAuthenticated, ],
    }

    def create_photo_session(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить фотосессию')
        profile = Profile.objects.get(user=request.user)
        serializer = PhotoSessionCreateSerializer(data=request.data | {"profile": profile.id})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно создал фотосессию')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не смог добавить фотосессию')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Создание фотосессию не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]