from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q
from geopy.distance import geodesic
from services.gallery_service import filter_queryset_by_param


def filter_gallery_by_distance(queryset, user_coordinates, distance):
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
        return queryset.filter(id__in=filter_queryset).select_related('gallery_image', 'profile')
    except ValueError:
        return []


def filter_gallery_by_category(queryset, category):
    """
    Фильтрация фото по категории
    """
    if not category:
        return queryset
    return queryset.filter(category__name_spec=category).select_related('gallery_image', 'profile')


def filter_gallery_by_words(queryset, search_words):
    """
    Фильтрация фото названию
    """
    search_words = search_words.split()
    if not search_words:
        return queryset
    if len(search_words) == 1:
        search_words = search_words[0]
        queryset = queryset.filter(
            (Q(name_image__icontains=search_words) |
             Q(description__icontains=search_words)))\
            .select_related('gallery_image', 'profile')
        return queryset
    else:
        search_vector = SearchVector("name_image", "description")
        search_query = SearchQuery(" | ".join(search_words), search_type="raw")
        return queryset.annotate(search=search_vector).filter(search=search_query)\
            .select_related('gallery_image', 'profile')


def filter_gallery_queryset(queryset, get_parameters):
    """
    Функцию сбора всех фильтраций в один queryset, а так же сортировка
    """
    queryset = filter_gallery_by_category(queryset,
                                          get_parameters.get('category', ''))
    queryset = filter_gallery_by_distance(queryset,
                                          get_parameters.get('user_coords'),
                                          get_parameters.get('distance'))
    filter_queryset = filter_gallery_by_words(queryset, get_parameters.get('search_words', ''))
    return filter_queryset_by_param(filter_queryset,
                                    get_parameters.get('sort_type', ''),
                                    get_parameters.get('filter_field', ''))