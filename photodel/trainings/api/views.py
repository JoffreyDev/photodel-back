from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from services.training_service import filter_trainings_queryset
from trainings.models import TrainingCategory, Trainings, TrainingsLike, \
    TrainingsComment, TrainingsFavorite, TrainingsRequest
from accounts.models import Profile
from .serializers import Trainings, TrainingCategory, \
    TrainingsAllLisForMaptSerializer, TrainingsFavoriteListSerializer, TrainingsLikeCreateSerializer, \
    TrainingsCommentCreateSerializer, TrainingsCommentListSerializer, TrainingsForCardSerializer, \
    TrainingsListSerializer, TrainingsAllListSerializer, \
    TrainingsRetrieveSerializer, \
    TrainingsAllLisForMaptSerializer, TrainingsUpdateSerializer, CategoryTrainingsListSerializer, TrainingsCreateSerializer, TrainingsFavoriteCreateSerializer, TrainingCreateRequestSerializer, TrainingsInvitesList, TrainingRequestChangeSerializer
from services.gallery_service import is_unique_favorite, is_unique_like, \
    protection_cheating_views, add_view, filter_queryset_by_param
from services.film_places_search_service import filter_film_places_queryset
from services.training_service import update_training_request_status
from tasks.accounts_task import task_send_email_to_verify_not_auth_request
from services.accounts_service import create_random_code, custom_paginator, create_notification
from services.request_chat_service import create_request_chat_and_message
from services.film_places_service import get_popular_places, update_not_auth_code, \
    validate_confirmation_code, check_user_allow_give_request
from services.ip_service import get_ip

import logging

logger = logging.getLogger(__name__)


class TrainingCategoryViewSet(viewsets.ViewSet):
    """
    Класс для представления работы с моделью TrainingCategory
    """

    def list_category(self, request):
        queryset = TrainingCategory.objects.order_by('name_category')
        serializer = CategoryTrainingsListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TrainingsViewSet(viewsets.ViewSet):
    """
    Класс для представления работы с моделью Trainings
    """
    permission_classes_by_action = {
        'create_training': [permissions.IsAuthenticated, ],
        'partial_update_training': [permissions.IsAuthenticated, ],
        'delete_training': [permissions.IsAuthenticated, ],
    }

    def create_training(self, request):
        logger.info(f'Пользователь {request.user} хочет создать обучение')
        profile = Profile.objects.get(user=request.user)
        if isinstance(request.data.get('training_images'), list) and len(request.data.get('training_images')) > 10:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": 'Создание обучения не было выполнено. '
                                             'Максимальное количество фотографий равно 10'})
        serializer = TrainingsCreateSerializer(data=request.data | {"profile": profile.id},
                                               context={'profile': profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info(
                f'Пользователь {request.user} успешно создал обучение')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не смог добавить обучение')
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Создание обучения не было выполнено '
                                                                 'Пожалуйства обратитесь в поддержку')

    def partial_update_training(self, request, pk):
        try:
            logger.info(f'Пользователь {request.user} хочет изменить обучение')
            profile = Profile.objects.get(user=request.user)
            instance = Trainings.objects.get(pk=pk, profile=profile)
            serializer = TrainingsUpdateSerializer(instance, data=request.data, partial=True,
                                                   context={'profile': profile})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                logger.info(
                    f'Пользователь {request.user} успешно изменил обучение')
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(
                f'Обновление обучение для пользователя {request.user} не было выполнено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Обновление обучение не было выполнено '
                                                                     'Пожалуйства обратитесь в поддержку')
        except Trainings.DoesNotExist:
            logger.error(
                f'обучение для пользователя {request.user} не было найдено')
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Обучение не было найдено")

    def retrieve_training(self, request, pk):
        try:
            user_ip = get_ip(request)
            instance = Trainings.objects.get(id=pk)
            if protection_cheating_views(instance, user_ip):
                add_view(instance)
            serializer = TrainingsRetrieveSerializer(
                instance, context={'user': request.user})
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Trainings.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'обучение не было найдено'})

    def list_training(self, request, pk):
        trainings = Trainings.objects.filter(profile=pk)
        queryset = filter_queryset_by_param(trainings,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', ''))
        serializer = TrainingsForCardSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_all_training(self, request):
        places = Trainings.objects.filter(is_hidden=False)
        queryset_filter = filter_trainings_queryset(places, request.GET)
        queryset = custom_paginator(queryset_filter, request)
        serializer = TrainingsAllListSerializer(queryset, many=True,
                                                context={'user_coords': request.GET.get('user_coords')})
        count_filter_items = len(queryset_filter)
        response_data = serializer.data
        if isinstance(response_data, list):
            response_data = {'data': response_data}

        response_data['totalCount'] = count_filter_items

        return Response(status=status.HTTP_200_OK, data=response_data)

    def list_all_training_for_map(self, request):
        places = Trainings.objects.filter(is_hidden=False)
        queryset = filter_film_places_queryset(places, request.GET)
        serializer = TrainingsAllLisForMaptSerializer(queryset, many=True,
                                                      context={'user_coords': request.GET.get('user_coords')})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete_training(self, request):
        try:
            trainings = request.data.get('trainings_id')
            for training in trainings:
                instance = Trainings.objects.get(
                    id=training, profile__user=request.user)
                instance.delete()
            return Response(status=status.HTTP_200_OK)
        except Trainings.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'обучение не было найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class TrainingsFavoriteViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_favorite': [permissions.IsAuthenticated, ],
        'delete_favorite': [permissions.IsAuthenticated, ],
    }

    def list_favorite(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список избранных обучений')
        favorites = TrainingsFavorite.objects.filter(profile_id=pk)
        queryset = filter_queryset_by_param(favorites,
                                            request.GET.get('sort_type', ''),
                                            request.GET.get('filter_field', '')) \
            .select_related('profile', 'training')
        serializer = TrainingsFavoriteListSerializer(queryset, many=True,
                                                     context={'user_coords': request.GET.get('user_coords')})
        logger.info(
            f'Пользователь {request.user} успешно получил список обучений')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_favorite(self, request):
        logger.info(
            f'Пользователь {request.user} хочет добавить обучение в избранное')
        profile = Profile.objects.get(user=request.user).id
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = Trainings.objects.get(
            pk=request.data.get('training')).profile

        if not is_unique_favorite(request.data.get('training'), profile, 'trainings'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":
                                                                      'Такое обучение уже есть в избранном'})
        serializer = TrainingsFavoriteCreateSerializer(
            data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(
                receiver_profile=owner_profile, sender_profile=sender_profile_instance, type='NEW_TRAINING_FAVORITE', action_position=request.data.get('training'))
            logger.info(
                f'Пользователь {request.user} учпешно добавил обучение в избранное')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил обучение в избранное')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление избранного не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_favorite(self, request):
        try:
            logger.info(
                f'Пользователь {request.user} хочет удалить обучение из избранного')
            training_favorites = request.data.get('training_favorites')
            profile = Profile.objects.get(user=request.user)
            for training in training_favorites:
                instance = TrainingsFavorite.objects.get(
                    profile=profile, training=training)
                instance.delete()
            logger.info(
                f'Пользователь {request.user} успешно удалил обучение из избранного')
            return Response(status=status.HTTP_200_OK)
        except TrainingsFavorite.DoesNotExist:
            logger.error(
                f'Для Пользователя {request.user} не было найдено избранное обучение при удалении')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Избранное обучение не было найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class TrainingsLikeViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_like': [permissions.IsAuthenticated, ],
        'delete_like': [permissions.IsAuthenticated, ],
    }

    def create_like(self, request):
        logger.info(
            f'Пользователь {request.user} хочет добавить лайк к обучению')
        profile = Profile.objects.get(user=request.user).id
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = Trainings.objects.get(
            pk=request.data.get('training')).profile
        if not is_unique_like(request.data.get('training'), profile, 'trainings'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Лайк обучении уже есть'})
        serializer = TrainingsLikeCreateSerializer(
            data=request.data | {"profile": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(
                receiver_profile=owner_profile, sender_profile=sender_profile_instance, type='NEW_TRAINING_LIKE', action_position=request.data.get('training'))
            logger.info(
                f'Пользователь {request.user} успешно добавил лайк к обучению')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил лайк к обучению')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление лайка не было выполнено. '
                                                                             'Пожалуйства обратитесь в поддержку'})

    def delete_like(self, request, pk):
        try:
            logger.info(
                f'Пользователь {request.user} хочет убрать лайк с обучения')
            profile = Profile.objects.get(user=request.user)
            instance = TrainingsLike.objects.get(profile=profile, training=pk)
            instance.delete()
            logger.info(
                f'Пользователь {request.user} успешно убрал лайк с обучения')
            return Response(status=status.HTTP_200_OK)
        except TrainingsLike.DoesNotExist:
            logger.error(
                f'Для Пользователя {request.user} не было найдено обучение при удалении лайка')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'обучение не было найдено'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class TrainingsCommentViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_comment': [permissions.IsAuthenticated, ],
    }

    def list_comments(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список  обучений')
        queryset = TrainingsComment.objects.filter(
            training=pk).select_related()
        serializer = TrainingsCommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_comment(self, request):
        logger.info(
            f'Пользователь {request.user} хочет создать комментарий к обучению')
        profile = Profile.objects.get(user=request.user).id
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = Trainings.objects.get(
            pk=request.data.get('training')).profile
        serializer = TrainingsCommentCreateSerializer(
            data=request.data | {"sender_comment": profile})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(
                receiver_profile=owner_profile, sender_profile=sender_profile_instance, type='NEW_TRAINING_COMMENT', action_position=request.data.get('training'))
            logger.info(
                f'Пользователь {request.user} успешно добавил комментарий к обучению')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Пользователь {request.user} не добавил комментарий к обучению')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'Добавление комментария не было выполнено.'
                                                                             ' Пожалуйства обратитесь в поддержку'})
    
    def edit_comment(self, request):
        comment_id = request.data.get('comment_id')
        try:
            comment = TrainingsComment.objects.get(pk=comment_id)
        except TrainingsComment.DoesNotExist:
            logger.error(f'Комментарий с ID {comment_id} не найден')
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": 'Комментарий не найден'})

        # Проверка, что текущий пользователь является автором комментария
        if comment.sender_comment.user != request.user:
            logger.error(f'Пользователь {request.user} попытался редактировать чужой комментарий')
            return Response(status=status.HTTP_403_FORBIDDEN, data={"message": 'Вы не можете редактировать этот комментарий'})

        serializer = TrainingsCommentCreateSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            logger.info(f'Пользователь {request.user} успешно отредактировал комментарий с ID {comment_id}')
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.error(f'Пользователь {request.user} не смог отредактировать комментарий с ID {comment_id}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_comment(self, request):
        comment_id = request.data.get('comment_id')
        try:
            comment = TrainingsComment.objects.get(pk=comment_id)
        except TrainingsComment.DoesNotExist:
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


class TrainingRequestViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'create_request': [permissions.IsAuthenticated, ],
    }

    def send_training_request(self, request):
        logger.info(
            f'Пользователь {request.user} хочет отправить запрос на обучение')
        serializer = TrainingCreateRequestSerializer(
            data=request.data)
        sender_profile_instance = Profile.objects.get(user=request.user)
        owner_profile = Trainings.objects.get(
            pk=request.data.get('training')).profile
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_notification(sender_profile=sender_profile_instance, receiver_profile=owner_profile,
                                type='NEW_TRAINING_REQUEST', action_position=request.data.get('training'))
            logger.info(
                f'Пользователь {request.user} успешно создал запрос на обучение')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'Пользователь {request.user} не создал запрос')
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": 'Cоздание запроса не было выполнено.'
                                                                  ' Пожалуйства обратитесь в поддержку'})

    def list_incoming_requests(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список запросов на обучение')
        profile = Profile.objects.get(pk=pk)
        requests = TrainingsRequest.objects.all()
        queryset = requests.filter(training__profile__id=pk)

        serializer = TrainingsInvitesList(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_outgoing_requests(self, request, pk):
        logger.info(
            f'Пользователь {request.user} хочет получить список  запросов на обучение')

        queryset = TrainingsRequest.objects.filter(request_user__id=pk)
        serializer = TrainingsInvitesList(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def change_request_status(self, request):
        logger.info(
            f'Пользователь {request.user} хочет изменить статус запроса на обучение')
        serializer = TrainingRequestChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        response = update_training_request_status(
            data=serializer_data, user=request.user)
        if request.data.get('status') == 'ACCEPTED':
            current_request = TrainingsRequest.objects.filter(
                id=request.data.get('request_id')).first()
            sender_profile = Profile.objects.get(
                user=current_request.request_user.user)
            training = Trainings.objects.get(pk=current_request.training.id)
            training.training_members.add(sender_profile)
        return Response(*response)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
