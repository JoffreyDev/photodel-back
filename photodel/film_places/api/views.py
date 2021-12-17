from rest_framework import generics, permissions, status, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from film_places.api.serializers import FilmPlacesCreateSerializer, CategoryFilmPlacesListSerializer
from film_places.models import CategoryFilmPlaces, FilmPlaces, Favorite
from accounts.models import Profile
from services.ip_service import get_ip

import logging

logger = logging.getLogger(__name__)


class CategoryFilmPlacesViewSet(viewsets.ViewSet):
    """
    Класс для представления работы с моделью CategoryFilmPlaces
    """
    def list_category(self, request):
        queryset = CategoryFilmPlaces.objevts.all()
        serializer = FilmPlacesCreateSerializer(queryset, many=True)
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

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]