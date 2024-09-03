from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from film_places.models import CategoryFilmPlaces, FilmPlaces, FilmPlacesFavorite, \
    FilmPlacesComment, FilmPlacesLike, FilmRequest, NotAuthFilmRequest
from accounts.models import Profile
from .serializers import FilmPlacesCreateSerializer, CategoryFilmPlacesListSerializer, \
    FilmPlacesFavoriteCreateSerializer, FilmPlacesFavoriteListSerializer, FilmPlacesLikeCreateSerializer, \
    FilmPlacesCommentCreateSerializer, FilmPlacesCommentListSerializer, FilmPlacesForCardSerializer, \
    FilmPlacesListSerializer, FilmRequestCreateSerializer, FilmPlacesAllListSerializer, \
    FilmPlacesRetrieveSerializer, NotAuthFilmRequestCreateSerializer, NotAuthFilmRequestListSerializer, \
    FilmPlacesAllLisForMaptSerializer, FilmRequestListSerializer, FilmPlacesUpdateSerializer
from services.gallery_service import is_unique_favorite, is_unique_like, \
    protection_cheating_views, add_view, filter_queryset_by_param
from services.film_places_search_service import filter_film_places_queryset
from tasks.accounts_task import task_send_email_to_verify_not_auth_request
from services.accounts_service import create_random_code, custom_paginator, create_notification
from services.request_chat_service import create_request_chat_and_message
from services.film_places_service import get_popular_places, update_not_auth_code, \
    validate_confirmation_code, check_user_allow_give_request
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
            logger.info(
                f'Пользователь {request.user} успешно создал место для съемки')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не смог добавить место для съемки')
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Создание места для съемки не было выполнено '
                                                                 'Пожалуйства обратитесь в поддержку')

    def partial_update_place(self, request, pk):
        try:
            logger.info(
                f'Пользователь {request.user} хочет изменить место съемки')
            profile = Profile.objects.get(user=request.user)
            instance = FilmPlaces.objects.get(pk=pk, profile=profile)
            serializer = FilmPlacesUpdateSerializer(instance, data=request.data, partial=True,
                                                    context={'profile': profile})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(
                    f'Пользователь {request.user} успешно изменил место съемки')
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(
                f'Обновление место съемки для пользователя {request.user} не было выполнено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Обновление место съемки не было выполнено '
                                                                     'Пожалуйства обратитесь в поддержку')
        except FilmPlaces.DoesNotExist:
            logger.error(
                f'место съемки для пользователя {request.user} не было найдено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Vесто съемки не было найдено")

    def retrieve_place(self, request, pk):
        try:
            user_ip = get_ip(request)
            instance = FilmPlaces.objects.get(id=pk)
            if protection_cheating_views(instance, user_ip):
                add_view(instance)
            serializer = FilmPlacesRetrieveSerializer(
                instance, context={'user': request.user})
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
        queryset_filter = filter_film_places_queryset(places, request.GET)
        queryset = custom_paginator(queryset_filter, request)
        serializer = FilmPlacesAllListSerializer(queryset, many=True,
                                                 context={'user_coords': request.GET.get('user_coords')})
        return Response(status=status.HTTP_200_OK, data=serializer.data,
                        headers={'Count-Filter-Items': len(queryset_filter)})

    def list_all_place_for_map(self, request):
        places = FilmPlaces.objects.filter(is_hidden=False)
        queryset = filter_film_places_queryset(places, request.GET)
        serializer = FilmPlacesAllLisForMaptSerializer(queryset, many=True,
                                                       context={'user_coords': request.GET.get('user_coords')})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete_place(self, request):
        try:
            places = request.data.get('places_id')
            for place in places:
                instance = FilmPlaces.objects.get(
                    id=place, profile__user=request.user)
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
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список избранных мест съемки')
        favorites = FilmPlacesFavorite.objects.filter(profile_id=pk)
        queryset = filter_queryset_by_param(favorites,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', '')) \
            .select_related('profile', 'place')
        serializer = FilmPlacesFavoriteListSerializer(queryset, many=True,
                                                      context={'user_coords': request.GET.get('user_coords')})
        logger.info(
            f'Пользователь {request.user} успешно получил список мест съемок')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(
            f'Пользователь {request.user} хочет добавить место съемки в избранное')
        profile = Profile.objects.get(user=request.user).id
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = FilmPlaces.objects.get(
            pk=request.data.get('place')).profile
        if not is_unique_favorite(request.data.get('place'), profile, 'places'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":
                                                                      'Такое место съемки уже есть в избранном'})
        serializer = FilmPlacesFavoriteCreateSerializer(
            data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(
                receiver_profile=owner_profile, sender_profile=sender_profile_instance, type='NEW_PLACE_FAVORITE', action_position=request.data.get('place'))
            logger.info(
                f'Пользователь {request.user} уcпешно добавил место съемки в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил место съемки в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request):
        try:
            logger.info(
                f'Пользователь {request.user} хочет удалить место съемки из избранного')
            place_favorites = request.data.get('place_favorites')
            profile = Profile.objects.get(user=request.user)
            for place in place_favorites:
                instance = FilmPlacesFavorite.objects.get(
                    profile=profile, place=place)
                instance.delete()
            logger.info(
                f'Пользователь {request.user} успешно удалил место съемки из избранного')
            return Response(status=status.HTTP_200_OK)
        except FilmPlacesFavorite.DoesNotExist:
            logger.error(
                f'Для Пользователя {request.user} не было найдено избранное место съемки при удалении')
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
        logger.info(
            f'Пользователь {request.user} хочет добавить лайк к месту съемки')
        profile = Profile.objects.get(user=request.user).id
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = FilmPlaces.objects.get(
            pk=request.data.get('place')).profile
        if not is_unique_like(request.data.get('place'), profile, 'places'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Лайк на месте съемки уже есть'})
        serializer = FilmPlacesLikeCreateSerializer(
            data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(
                receiver_profile=owner_profile, sender_profile=sender_profile_instance, type='NEW_PLACE_LIKE', action_position=request.data.get('place'))
            logger.info(
                f'Пользователь {request.user} успешно добавил лайк к месту съемки')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил лайк к месту съемки')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(
                f'Пользователь {request.user} хочет убрать лайк с места съемки')
            profile = Profile.objects.get(user=request.user)
            instance = FilmPlacesLike.objects.get(profile=profile, place=pk)
            instance.delete()
            logger.info(
                f'Пользователь {request.user} успешно убрал лайк с места съемки')
            return Response(status=status.HTTP_200_OK)
        except FilmPlacesLike.DoesNotExist:
            logger.error(
                f'Для Пользователя {request.user} не было найдено место съемки при удалении лайка')
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
        logger.info(
            f'Пользователь {request.user} хочет получить список мест съемок')
        queryset = FilmPlacesComment.objects.filter(place=pk).select_related()
        serializer = FilmPlacesCommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        logger.info(
            f'Пользователь {request.user} хочет создать комментарий к месту съемки')
        profile = Profile.objects.get(user=request.user).id
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = FilmPlaces.objects.get(
            pk=request.data.get('place')).profile
        serializer = FilmPlacesCommentCreateSerializer(
            data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(
                receiver_profile=owner_profile, sender_profile=sender_profile_instance, type='NEW_PLACE_COMMENT', action_position=request.data.get('place'))
            logger.info(
                f'Пользователь {request.user} успешно добавил комментарий к месту съемки')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил комментарий к месту съемки')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})
    
    def edit_comment(self, request):
        comment_id = request.data.get('comment_id')
        try:
            comment = FilmPlacesComment.objects.get(pk=comment_id)
        except FilmPlacesComment.DoesNotExist:
            logger.error(f'Комментарий с ID {comment_id} не найден')
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": 'Комментарий не найден'})

        # Проверка, что текущий пользователь является автором комментария
        if comment.sender_comment.user != request.user:
            logger.error(f'Пользователь {request.user} попытался редактировать чужой комментарий')
            return Response(status=status.HTTP_403_FORBIDDEN, data={"message": 'Вы не можете редактировать этот комментарий'})

        serializer = FilmPlacesCommentCreateSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно отредактировал комментарий с ID {comment_id}')
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.error(f'Пользователь {request.user} не смог отредактировать комментарий с ID {comment_id}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_comment(self, request):
        comment_id = request.data.get('comment_id')
        try:
            comment = FilmPlacesComment.objects.get(pk=comment_id)
        except FilmPlacesComment.DoesNotExist:
            logger.error(f'Комментарий с ID {comment_id} не найден')
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": 'Комментарий не найден'})

        # Проверка, что текущий пользователь является автором комментария
        if comment.sender_comment.user != request.user:
            logger.error(f'Пользователь {request.user} попытался редактировать чужой комментарий')
            return Response(status=status.HTTP_403_FORBIDDEN, data={"message": 'Вы не можете редактировать этот комментарий'})
        
        comment.delete()
        return Response(status=status.HTTP_200_OK)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FilmRequestViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_film_request': [permissions.IsAuthenticated, ],
        'add_reason_failure': [permissions.IsAuthenticated, ],
    }

    def create_film_request(self, request):
        logger.info(f'Пользователь {request.user} хочет создать запрос')
        profile = Profile.objects.get(user=request.user).id
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = Profile.objects.get(
            pk=request.data.get('receiver_profile'))
        serializer = FilmRequestCreateSerializer(
            data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(sender_profile=sender_profile_instance, receiver_profile=owner_profile,
                                type='NEW_FILMING_REQUEST', action_position=0)
            create_request_chat_and_message(serializer.data.get('profile'),
                                            serializer.data.get(
                                                'receiver_profile'),
                                            serializer.data.get('id'))
            logger.info(f'Пользователь {request.user} успешно создал запрос')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не создал запрос')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'создание запроса не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def list_incoming_request(self, request, pk):
        queryset = FilmRequest.objects.filter(receiver_profile_id=pk)\
            .select_related('profile', 'receiver_profile')
        serializer = FilmRequestListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_outgoing_request(self, request, pk):
        queryset = FilmRequest.objects.filter(profile_id=pk)\
            .select_related('profile', 'receiver_profile')
        serializer = FilmRequestListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def add_reason_failure(self, request, pk):
        try:
            instance = FilmRequest.objects.get(id=pk)
            if request.user != instance.profile.user or instance.filming_status != 'UNCOMPLETED':
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": 'Только заказчик может добавить причину не завершенного запроса'})
            instance.reason_failure = request.data.get('reason_failure', '')
            instance.save()
            return Response(status=status.HTTP_200_OK, data={"message": 'Причина не заверщенного заказа '
                                                                        'была успещно добавлена'})
        except FilmRequest.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Запрос не был найден.'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class NotAuthFilmRequestViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'list_not_auth_requests': [permissions.IsAuthenticated, ],
        'retrieve_not_auth_requests': [permissions.IsAuthenticated, ],
    }

    def create_not_auth_film_request(self, request):
        if not check_user_allow_give_request(request.data.get('email', '')):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": 'Вы можете отправлять запросы только раз в день'})
        serializer = NotAuthFilmRequestCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            code = create_random_code(6)
            update_not_auth_code(serializer.data.get('id', ''), code)
            task_send_email_to_verify_not_auth_request(
                serializer.data.get('email', ''), code)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'создание запроса не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})

    def confirm_email(self, request):
        if not validate_confirmation_code(request.data.get('email', ''), request.data.get('code', '')):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Проверка не была выполнена. '
                                                                                 'Запрос не был отправлен исполнителю'})
        return Response(status=status.HTTP_200_OK, data={"message": 'создание запроса было выполнено'})

    def list_not_auth_requests(self, request):
        queryset = NotAuthFilmRequest.objects.filter(receiver_profile__user=request.user, email_verify=True)\
            .select_related('receiver_profile')
        serializer = NotAuthFilmRequestListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve_not_auth_requests(self, request, pk):
        try:
            queryset = NotAuthFilmRequest.objects.get(
                id=pk, receiver_profile__user=request.user, email_verify=True)
            serializer = NotAuthFilmRequestListSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotAuthFilmRequest.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Запрос не был найден"})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
