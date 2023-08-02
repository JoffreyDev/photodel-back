from django.contrib.postgres.search import SearchVector, SearchQuery
from services.accounts_service import filter_queryset_by_param
from geopy.distance import geodesic
from django.db.models import Q
from channels.db import database_sync_to_async
from trainings.models import TrainingsRequest
from django.db.models import Q, When, Case
from asgiref.sync import sync_to_async
from datetime import timedelta
import json


def update_training_request_status(data, user):
    """
    Updating film request status
    Args:
        data: data from request
        user: current user
    Returns:
        current response data, status
    """

    request = TrainingsRequest.objects.get(id=data['request_id'])
    status = data['status']
    current_status = request.status
    if current_status == 'AWAITING' and (user in request.training.training_orgs.all() or user == request.training.profile.user) and status in ['ACCEPTED', 'REJECTED']:
        request.status = status
        request.save()
        return {'message': 'Статус успешно изменен!'}, 200
    return {'error': f' У вас нет прав для изменения статуса приглашения'}, 403


def filter_trainings_by_distance(queryset, user_coordinates, distance):
    """
    Фильтрация фото по расстоянию от пользователя
    """
    if not (user_coordinates or distance):
        return queryset
    filter_queryset = []
    try:
        for query in queryset:
            distance_diff = geodesic(query.place_location, user_coordinates).m
            if float(distance) > float(distance_diff):
                filter_queryset.append(query.id)
        return queryset.filter(id__in=filter_queryset)
    except ValueError:
        return []


def filter_trainings_by_category(queryset, category):
    """
    Фильтрация фото по категории
    """
    if not category:
        return queryset
    return queryset.filter(training_category__name_category=category)


def filter_trainings_by_words(queryset, search_words):
    """
    Фильтрация фото названию
    """
    search_words = search_words.split()
    if not search_words:
        return queryset
    if len(search_words) == 1:
        search_words = search_words[0]
        queryset = queryset.filter(
            (Q(training_title__icontains=search_words) |
             Q(training_description__icontains=search_words)))\

        return queryset
    else:
        search_vector = SearchVector("training_title", "training_description")
        search_query = SearchQuery(" | ".join(search_words), search_type="raw")
        return queryset.annotate(search=search_vector).filter(search=search_query)\



def filter_trainings_queryset(queryset, get_parameters):
    """
    Функцию сбора всех фильтраций в один queryset, а так же сортировка
    """
    queryset = filter_trainings_by_category(queryset,
                                            get_parameters.get('category', ''))
    queryset = filter_trainings_by_distance(queryset,
                                            get_parameters.get('user_coords'),
                                            get_parameters.get('distance'))
    filter_queryset = filter_trainings_by_words(
        queryset, get_parameters.get('search_words', ''))
    return filter_queryset_by_param(filter_queryset,
                                    get_parameters.get('sort_type', ''),
                                    get_parameters.get('filter_field', ''))
