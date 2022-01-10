from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from film_places.models import CategoryFilmPlaces, FilmPlaces, FilmPlacesFavorite, FilmPlacesComment, FilmPlacesLike
from accounts.models import Profile
from .serializers import FilmPlacesCreateSerializer, CategoryFilmPlacesListSerializer, \
    FilmPlacesFavoriteCreateSerializer, FilmPlacesFavoriteListSerializer, FilmPlacesLikeCreateSerializer, \
    FilmPlacesCommentCreateSerializer, FilmPlacesCommentListSerializer
from services.gallery_service import is_unique_favorite, is_unique_like
from services.ip_service import get_ip

import logging

logger = logging.getLogger(__name__)


class CategoryFilmPlacesViewSet(viewsets.ViewSet):
    """
    Класс для представления работы с моделью CategoryFilmPlaces
    """
    def list_category(self, request):
        queryset = CategoryFilmPlaces.objevts.all()
        serializer = CategoryFilmPlacesListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilmPlacesViewSet(viewsets.ViewSet):
    """
    Класс для представления работы с моделью FilmPlaces
    """
    permission_classes_by_action = {
        'create_place': [permissions.IsAuthenticated, ],
        }

    def create_place(self, request):
        try:
            logger.info(f'Пользователь {request.user} хочет создать место съемки')
            profile = Profile.objects.get(user=request.user)
            serializer = FilmPlacesCreateSerializer(data=request.data | {"profile": profile.id})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(f'Пользователь {request.user} успешно создал место для съемки')
                return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            logger.error(f'У Пользователя {request.user} ошибка с параметрами')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Не были переданы координаты '
                                                                     'Пожалуйства обратитесь в поддержку')
        logger.error(f'Пользователь {request.user} не смог добавить место для съемки')
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Создание места для съемки не было выполнено '
                                                                 'Пожалуйства обратитесь в поддержку')

    def list_places(self, request):
        pass

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FilmPlacesFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated, ],
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет получить список избранных мест съемки')
        queryset = FilmPlacesFavorite.objects.filter(profile__user=request.user).select_related()
        serializer = FilmPlacesFavoriteListSerializer(queryset, many=True)
        logger.info(f'Пользователь {request.user} успешно получил список мест съемок')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить место съемки в избранное')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_favorite(request.data.get('place'), profile, 'places'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":
                                                                      'Такое место съемки уже есть в избранном'})
        serializer = FilmPlacesFavoriteCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} учпешно добавил место съемки в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил место съемки в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет удалить место съемки из избранного')
            profile = Profile.objects.get(user=request.user)
            instance = FilmPlacesFavorite.objects.get(profile=profile.id, place=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно удалил место съемки из избранного')
            return Response(status=status.HTTP_200_OK)
        except FilmPlacesFavorite.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено избранное место съемки при удалении')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Избранное мест съемки не было найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FilmPlacesLikeViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_like': [permissions.IsAuthenticated, ],
        'delete_like': [permissions.IsAuthenticated, ],
    }

    def create_like(self, request):
        logger.info(f'Пользователь {request.user} хочет добавить лайк к месту съемки')
        profile = Profile.objects.get(user=request.user).id
        if not is_unique_like(request.data.get('place'), profile, 'places'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Лайк на месте съемки уже есть'})
        serializer = FilmPlacesLikeCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил лайк к месту съемки')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил лайк к месту съемки')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет убрать лайк с места съемки')
            profile = Profile.objects.get(user=request.user)
            instance = FilmPlacesLike.objects.get(profile=profile, place=pk)
            instance.delete()
            logger.info(f'Пользователь {request.user} успешно убрал лайк с места съемки')
            return Response(status=status.HTTP_200_OK)
        except FilmPlacesLike.DoesNotExist:
            logger.error(f'Для Пользователя {request.user} не было найдено место съемки при удалении лайка')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Место съемки не была найдена'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FilmPlacesCommentViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_comments(self, request, pk):
        logger.info(f'Пользователь {request.user} хочет получить список мест съемок')
        queryset = FilmPlacesComment.objects.filter(place=pk).select_related()
        serializer = FilmPlacesCommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        logger.info(f'Пользователь {request.user} хочет создать комментарий к месту съемки')
        profile = Profile.objects.get(user=request.user).id
        serializer = FilmPlacesCommentCreateSerializer(data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно добавил комментарий к месту съемки')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не добавил комментарий к месту съемки')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]