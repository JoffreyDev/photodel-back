from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from gallery.models import Album, Gallery, Image, GalleryComment, GalleryLike, GalleryFavorite, \
    PhotoSessionComment, PhotoSessionLike, PhotoSessionFavorite, PhotoSession
from accounts.models import Profile
from services.gallery_service import is_unique_favorite, is_unique_like, \
    protection_cheating_views, add_view
from services.gallery_search_service import filter_gallery_queryset
from services.gallery_service import filter_queryset_by_param
from services.ip_service import get_ip
from .serializers import AlbumListSerializer, AlbumCreateSerializer, GalleryRetrieveSerializer, \
    GalleryForCardListSerializer, GalleryCreateSerializer, GalleryFavoriteCreateSerializer, \
    GalleryFavoriteListSerializer, GalleryLikeCreateSerializer, GalleryCommentListSerializer, \
    GalleryCommentCreateSerializer, PhotoSessionCreateSerializer, \
    AlbumUpdateSerializer, PhotoSessionFavoriteCreateSerializer, PhotoSessionFavoriteListSerializer, \
    PhotoSessionLikeCreateSerializer, PhotoSessionCommentListSerializer, \
    PhotoSessionCommentCreateSerializer, PhotoSessionForCardListSerializer, PhotoSessionListSerializer, \
    AlbumGalleryRetrieveSerializer, ImageCreateSerializer, GalleryAllListSerializer
from .permissions import IsOwnerImage, IsAddOrDeletePhotoFromAlbum, IsCreatePhoto

import logging

logger = logging.getLogger(__name__)


# вьюхи фото
class ImageViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_image': [permissions.IsAuthenticated, ],
        }

    def create_image(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ImageCreateSerializer(data=request.data | {"profile": profile.id})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление изображение не было выполнено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


# вьюхи альбомов
class AlbumViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_album': [permissions.IsAuthenticated, IsOwnerImage, ],
        'partial_update': [permissions.IsAuthenticated, ],
        'list_photos_not_in_album': [permissions.IsAuthenticated, ],
        'add_to_album_photos': [permissions.IsAuthenticated, IsAddOrDeletePhotoFromAlbum, ],
        'delete_from_album_photos': [permissions.IsAuthenticated, IsAddOrDeletePhotoFromAlbum, ],
        'delete_album': [permissions.IsAuthenticated, ],
        }

    def create_album(self, request):
        """
        Создание альбома
        """
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

    def partial_update(self, request, pk):
        """
        Частитичное или полное обновление полей в альбома
        """
        try:
            logger.info(f'Пользователь {request.user} хочет изменить альбом')
            profile = Profile.objects.get(user=request.user)
            instance = Album.objects.get(pk=pk, profile=profile)
            serializer = AlbumUpdateSerializer(instance, data=request.data, partial=True,
                                               context={'profile': profile, 'updated_album': instance})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(f'Пользователь {request.user} успешно изменил альбом')
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f'Обновление альбома для пользователя {request.user} не было выполнено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Обновление альбома не было выполнено.'
                                                                                 ' Пожалуйства обратитесь в поддержку'})
        except Album.DoesNotExist:
            logger.error(f'Альбом для пользователя {request.user} не был найден')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Альбом не был найден"})

    def list_user_albums(self, request, pk):
        """
        Список альбомов пользователя с помощью id профиля
        """
        albums = Album.objects.filter(profile=pk)
        queryset = filter_queryset_by_param(albums,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', ''))\
            .select_related('profile', 'main_photo_id')
        serializer = AlbumListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_album_photos(self, request, pk):
        """
        Список фото из альбома
        """
        galleries = Gallery.objects.filter(album=pk).select_related('gallery_image')
        serializer = GalleryForCardListSerializer(galleries, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve_album(self, request, pk):
        """
        Получение информации из одного альюома
        """
        try:
            album = Album.objects.get(id=pk)
            galleries = Gallery.objects.filter(album=album)
            serializer = AlbumGalleryRetrieveSerializer(galleries, many=True, context={"album": album})
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Альбом не был найден"})

    def list_photos_not_in_album(self, request, pk):
        """
        Список фоток не в альбоме
        """
        try:
            album = Album.objects.get(id=pk)
            galleries = Gallery.objects.filter(profile__user=request.user)\
                .exclude(id__in=[gallery.id for gallery in album.gallery_set.all()])\
                .select_related('gallery_image')
            serializer = GalleryForCardListSerializer(galleries, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Album.DoesNotExist:
            logger.error(f'Альбом для пользователя {request.user} не был найден')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Альбом не был найден"})

    def add_to_album_photos(self, request):
        """
        Добавление фото в альбом с помощью списка фото
        """
        try:
            if not request.data.get('album_id') or not request.data.get('photos_id'):
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Не были переданы обязательные '
                                                                          'параметры. Пожалуйства обратитесь '
                                                                          'в поддержку'})
            album = Album.objects.get(id=request.data.get('album_id'))
            for photo in request.data.get('photos_id'):
                gallery = Gallery.objects.get(id=photo)
                gallery.album.add(album)
                gallery.save()
            return Response(status=status.HTTP_200_OK)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Альбом не был найден. '
                                                                      'Пожалуйства обратитесь в поддержку'})
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото не было найдено. '
                                                                      'Пожалуйства обратитесь в поддержку'})

    def delete_from_album_photos(self, request):
        """
        Удаление фото из альбома с помощью списка фото
        """
        try:
            if not request.data.get('album_id') or not request.data.get('photos_id'):
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message" 'Не были переданы обязательные '
                                                                          'параметры. Пожалуйства обратитесь '
                                                                          'в поддержку'})
            album = Album.objects.get(id=request.data.get('album_id'))
            for photo in request.data.get('photos_id'):
                gallery = Gallery.objects.get(id=photo)
                gallery.album.remove(album)
                gallery.save()
            return Response(status=status.HTTP_200_OK)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message" 'Альбом не был найден. '
                                                                      'Пожалуйства обратитесь в поддержку'})
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message" 'Фото не было найдено. '
                                                                      'Пожалуйства обратитесь в поддержку'})

    def delete_album(self, request):
        """
        Удаление альбома/ов c помощью списка id
        """
        try:
            albums_id = request.data.get('albums_id')
            for album_id in albums_id:
                instance = Album.objects.get(id=album_id, profile__user=request.user)
                instance.delete()
            return Response(status=status.HTTP_200_OK)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Альбом не был найден'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


# вьюхи фото в галлерее
class GalleryViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_photo': [permissions.IsAuthenticated, IsCreatePhoto, ],
        'partial_update_photo': [permissions.IsAuthenticated, ],
        'delete_photo': [permissions.IsAuthenticated, ],
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

    def partial_update_photo(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет изменить фото')
            profile = Profile.objects.get(user=request.user)
            instance = Gallery.objects.get(pk=pk, profile=profile)
            serializer = GalleryCreateSerializer(instance, data=request.data, partial=True, context={'profile': profile})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(f'Пользователь {request.user} успешно изменил фото')
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f'Обновление фото для пользователя {request.user} не было выполнено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Обновление фото не было выполнено '
                                                                     'Пожалуйства обратитесь в поддержку')
        except Gallery.DoesNotExist:
            logger.error(f'Фото для пользователя {request.user} не было найдено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Фото не было найдено")

    def retrieve_photo(self, request, pk):
        try:
            user_ip = get_ip(request)
            instance = Gallery.objects.get(id=pk)
            if protection_cheating_views(instance, user_ip):
                add_view(instance)
            serializer = GalleryRetrieveSerializer(instance, context={"user": request.user})
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото из галерии не было найдено'})

    def popular_photos(self, request):
        photos = Gallery.objects.order_by('views').select_related('gallery_image')[:10]
        serializer = GalleryForCardListSerializer(photos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_photos(self, request, pk):
        photos = Gallery.objects.filter(profile=pk)
        queryset = filter_queryset_by_param(photos,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', ''))\
            .select_related('gallery_image')
        serializer = GalleryForCardListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_all_photos(self, request):
        photos = Gallery.objects.filter(is_hidden=False)
        queryset = filter_gallery_queryset(photos, request.GET)
        serializer = GalleryAllListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete_photo(self, request):
        try:
            photos_id = request.data.get('photos_id')
            for photo in photos_id:
                instance = Image.objects.get(id=Gallery.objects.get(id=photo)
                                             .gallery_image.id, profile__user=request.user)
                instance.delete()
            return Response(status=status.HTTP_200_OK)
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото не был найдено'})
        except Image.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фото не был найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class GalleryFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request, pk):
        logger.info(f'Пользователь {request.user} хочет получить список избранных фото')
        favorites = GalleryFavorite.objects.filter(profile_id=pk)
        queryset = filter_queryset_by_param(favorites,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', '')) \
            .select_related('profile', 'gallery')
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

    def delete_favorite(self, request):
        try:
            logger.info(f'Пользователь {request.user} хочет удалить фото из избранного')
            gallery_favorites = request.data.get('gallery_favorites')
            profile = Profile.objects.get(user=request.user)
            for gallery in gallery_favorites:
                instance = GalleryFavorite.objects.get(profile=profile, gallery=gallery)
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
        queryset = GalleryComment.objects.filter(gallery=pk).select_related('sender_comment', 'gallery')
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


# вьюхи фотосессий
class PhotoSessionViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_photo_session': [permissions.IsAuthenticated, ],
        'partial_update_photo_session': [permissions.IsAuthenticated, ],
        'delete_photo_session': [permissions.IsAuthenticated, ],
    }

    def create_photo_session(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить фотосессию')
        profile = Profile.objects.get(user=request.user)
        if isinstance(request.data.get('photos'), list) and len(request.data.get('photos')) > 10:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": 'Создание фотосессию не было выполнено. '
                                             'Максимальное количество фотографий равно 10'})
        serializer = PhotoSessionCreateSerializer(data=request.data | {"profile": profile.id},
                                                  context={'profile': profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно создал фотосессию')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не смог добавить фотосессию')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Создание фотосессию не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def partial_update_photo_session(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет изменить фотосессию')
            profile = Profile.objects.get(user=request.user)
            instance = PhotoSession.objects.get(pk=pk, profile=profile)
            serializer = PhotoSessionCreateSerializer(instance, data=request.data, partial=True,
                                                      context={'profile': profile})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(f'Пользователь {request.user} успешно изменил фотосессию')
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f'Обновление фотосессии для пользователя {request.user} не было выполнено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Обновление фотосессим не было выполнено '
                                                                     'Пожалуйства обратитесь в поддержку')
        except PhotoSession.DoesNotExist:
            logger.error(f'Фотосессия для пользователя {request.user} не было найдено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Фотосессия не было найдено")

    def retrieve_photo_session(self, request, pk):
        try:
            user_ip = get_ip(request)
            instance = PhotoSession.objects.get(id=pk)
            if protection_cheating_views(instance, user_ip):
                add_view(instance)
            serializer = PhotoSessionListSerializer(instance, context={"user": request.user})
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except PhotoSession.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фотосессия не была найдена'})

    def list_photo_sessions(self, request, pk):
        photo_sessions = PhotoSession.objects.filter(profile=pk)
        queryset = filter_queryset_by_param(photo_sessions,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', ''))
        serializer = PhotoSessionForCardListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete_photo_session(self, request):
        try:
            photo_sessions = request.data.get('photo_sessions_id')
            for photo_sessions in photo_sessions:
                instance = PhotoSession.objects.get(id=photo_sessions, profile__user=request.user)
                instance.delete()
            return Response(status=status.HTTP_200_OK)
        except PhotoSession.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фотосессия не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class PhotoSessionFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request, pk):
        logger.info(f'Пользователь {request.user} хочет получить список избранных фотосессий')
        favorites = PhotoSessionFavorite.objects.filter(profile_id=pk)
        queryset = filter_queryset_by_param(favorites,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', ''))\
            .select_related('photo_session__session_category', 'profile')
        serializer = PhotoSessionFavoriteListSerializer(queryset, many=True,
                                                        context={'user_coords': request.GET.get('user_coords')})
        logger.info(f'Пользователь {request.user} успешно получил список избранных фотосессий')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить фотосессию в избранное')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_favorite(request.data.get('photo_session'), profile, 'photo_session'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такая фотосессия уже есть в избранном'})
        serializer = PhotoSessionFavoriteCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил фотосессию в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил фотосессию в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request):
        try:
            logger.info(f'Пользователь {request.user} хочет удалить фотосессию из избранного')
            photo_session_favorites = request.data.get('photo_session_favorites')
            profile = Profile.objects.get(user=request.user)
            for photo_session in photo_session_favorites:
                instance = PhotoSessionFavorite.objects.get(profile=profile, photo_session=photo_session)
                instance.delete()
            logger.info(f'Пользователь {request.user} успешно удалил фотосессию из избранного')
            return Response(status=status.HTTP_200_OK)
        except PhotoSessionFavorite.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено избранная фотосессия при удалении')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Избранная фотосессия не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class PhotoSessionLikeViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_like': [permissions.IsAuthenticated, ],
        'delete_like': [permissions.IsAuthenticated, ],
    }

    def create_like(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить лайк к фотосессии')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_like(request.data.get('photo_session'), profile, 'photo_session'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Такой лайк на фотосессии уже есть'})
        serializer = PhotoSessionLikeCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил лайк к фотосессии')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил лайк к фотосессии')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет убрать лайк с фотосессии')
            profile = Profile.objects.get(user=request.user)
            instance = PhotoSessionLike.objects.get(profile=profile, photo_session=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно убрал лайк с фотосессии')
            return Response(status=status.HTTP_200_OK)
        except PhotoSessionLike.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено фотосессия при удалении лайка')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Фотосессия не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class PhotoSessionCommentViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_comments(self, request, pk):
        queryset = PhotoSessionComment.objects.filter(photo_session=pk)\
            .select_related('sender_comment', 'photo_session__session_category')
        serializer = PhotoSessionCommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        profile = Profile.objects.get(user=request.user).id
        serializer = PhotoSessionCommentCreateSerializer(data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил комментарий к фотосессии')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил комментарий к фотосессии')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]