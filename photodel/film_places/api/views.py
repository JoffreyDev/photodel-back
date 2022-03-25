from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from film_places.models import CategoryFilmPlaces, FilmPlaces, FilmPlacesFavorite, FilmPlacesComment, FilmPlacesLike
from accounts.models import Profile
from .serializers import FilmPlacesCreateSerializer, CategoryFilmPlacesListSerializer, \
    FilmPlacesFavoriteCreateSerializer, FilmPlacesFavoriteListSerializer, FilmPlacesLikeCreateSerializer, \
    FilmPlacesCommentCreateSerializer, FilmPlacesCommentListSerializer, FilmPlacesForCardSerializer, \
    FilmPlacesListSerializer, FilmRequestCreateSerializer, FilmPlacesAllListSerializer
from services.gallery_service import is_unique_favorite, is_unique_like, \
    protection_cheating_views, add_view, filter_queryset_by_param
from services.film_places_search_service import filter_film_places_queryset
from services.request_chat_service import create_request_chat_and_message
from services.film_places_service import get_popular_places
from services.ip_service import get_ip

import logging

logger = logging.getLogger(__name__)


class CategoryFilmPlacesViewSet(viewsets.ViewSet):
    """
    Класс для представления работы с моделью CategoryFilmPlaces
    """
    def list_category(self, request):
        queryset = CategoryFilmPlaces.objects.order_by('name_category')
        serializer = CategoryFilmPlacesListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilmPlacesViewSet(viewsets.ViewSet):
    """
    Класс для представления работы с моделью FilmPlaces
    """
    permission_classes_by_action = {
        'create_place': [permissions.IsAuthenticated, ],
        'partial_update_place': [permissions.IsAuthenticated, ],
        'delete_place': [permissions.IsAuthenticated, ],
        }

    def create_place(self, request):
        logger.info(f'Пользователь {request.user} хочет создать место съемки')
        profile = Profile.objects.get(user=request.user)
        if isinstance(request.data.get('place_image'), list) and len(request.data.get('place_image')) > 10:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": 'Создание места съемки не было выполнено. '
                                             'Максимальное количество фотографий равно 10'})
        serializer = FilmPlacesCreateSerializer(data=request.data | {"profile": profile.id},
                                                context={'profile': profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно создал место для съемки')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не смог добавить место для съемки')
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Создание места для съемки не было выполнено '
                                                                 'Пожалуйства обратитесь в поддержку')

    def partial_update_place(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет изменить место съемки')
            profile = Profile.objects.get(user=request.user)
            instance = FilmPlaces.objects.get(pk=pk, profile=profile)
            serializer = FilmPlacesCreateSerializer(instance, data=request.data, partial=True,
                                                    context={'profile': profile})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(f'Пользователь {request.user} успешно изменил место съемки')
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f'Обновление место съемки для пользователя {request.user} не было выполнено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Обновление место съемки не было выполнено '
                                                                     'Пожалуйства обратитесь в поддержку')
        except FilmPlaces.DoesNotExist:
            logger.error(f'место съемки для пользователя {request.user} не было найдено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Vесто съемки не было найдено")

    def retrieve_place(self, request, pk):
        try:
            user_ip = get_ip(request)
            instance = FilmPlaces.objects.get(id=pk)
            if protection_cheating_views(instance, user_ip):
                add_view(instance)
            serializer = FilmPlacesListSerializer(instance)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except FilmPlaces.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Место съемки не было найдено'})

    def list_place(self, request, pk):
        places = FilmPlaces.objects.filter(profile=pk)
        queryset = filter_queryset_by_param(places,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', ''))
        serializer = FilmPlacesForCardSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def the_best_places(self, request):
        category = request.GET.get('category')
        places = get_popular_places(category)
        serializer = FilmPlacesListSerializer(places, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_all_place(self, request):
        places = FilmPlaces.objects.filter(is_hidden=False)
        queryset = filter_film_places_queryset(places, request.GET)
        serializer = FilmPlacesAllListSerializer(queryset, many=True,
                                                 context={'user_coords': request.GET.get('user_coords')})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete_place(self, request):
        try:
            places = request.data.get('places_id')
            for place in places:
                instance = FilmPlaces.objects.get(id=place, profile__user=request.user)
                instance.delete()
            return Response(status=status.HTTP_200_OK)
        except FilmPlaces.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Место съемки не было найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FilmPlacesFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'list_favorite': [permissions.IsAuthenticated, ],
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request):
        logger.info(f'Пользователь {request.user} хочет получить список избранных мест съемки')
        favorites = FilmPlacesFavorite.objects.filter(profile__user=request.user)
        queryset = filter_queryset_by_param(favorites,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', '')) \
            .select_related('profile', 'place')
        serializer = FilmPlacesFavoriteListSerializer(queryset, many=True,
                                                      context={'user_coords': request.GET.get('user_coords')})
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

    def delete_favorite(self, request):
        try:
            logger.info(f'Пользователь {request.user} хочет удалить место съемки из избранного')
            place_favorites = request.data.get('place_favorites')
            profile = Profile.objects.get(user=request.user)
            for place in place_favorites:
                instance = FilmPlacesFavorite.objects.get(profile=profile, place=place)
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


class FilmRequestViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_film_request': [permissions.IsAuthenticated, ],
    }

    def create_film_request(self, request):
        logger.info(f'Пользователь {request.user} хочет создать запрос')
        profile = Profile.objects.get(user=request.user).id
        serializer = FilmRequestCreateSerializer(data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_request_chat_and_message(serializer.data.get('profile'), serializer.data.get('place'),
                                            serializer.data.get('id'))
            logger.info(f'Пользователь {request.user} успешно создал запрос')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не создал запрос')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'создание запроса не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]