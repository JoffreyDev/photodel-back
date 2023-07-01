from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q
from geopy.distance import geodesic
from services.accounts_service import filter_queryset_by_param


def filter_film_places_by_distance(queryset, user_coordinates, distance):
    """
    Фильтрация мест сьемок по расстоянию от пользователя
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


def filter_film_places_by_category(queryset, category):
    """
    Фильтрация мест сьемо по категории
    """
    if not category:
        return queryset
    return queryset.filter(category__name_category=category).select_related('profile').prefetch_related('place_image')


def filter_film_places_by_words(queryset, search_words):
    """
    Фильтрация мест сьемо названию
    """
    search_words = search_words.split()
    if not search_words:
        return queryset
    if len(search_words) == 1:
        search_words = search_words[0]
        queryset = queryset.filter(
            (Q(name_place__icontains=search_words) |
             Q(description__icontains=search_words)))\
            .select_related('profile').prefetch_related('place_image')
        return queryset
    else:
        search_vector = SearchVector("name_place", "description")
        search_query = SearchQuery(" | ".join(search_words), search_type="raw")
        return queryset.annotate(search=search_vector).filter(search=search_query)
    
def filter_place_by_place(queryset, place):
    """
    Фильтрация места по месту
    """
    if not place:
        return queryset
    queryset = queryset.filter(string_place_location__contains=place)
    return queryset


def filter_film_places_queryset(queryset, get_parameters):
    """
    Функцию сбора всех фильтраций в один queryset, а так же сортировка
    """
    queryset = filter_film_places_by_category(queryset,
                                              get_parameters.get('category', ''))
    queryset = filter_film_places_by_distance(queryset,
                                              get_parameters.get(
                                                  'user_coords'),
                                              get_parameters.get('distance'))
    queryset = filter_film_places_by_words(
        queryset, get_parameters.get('search_words', ''))
    
    queryset = filter_place_by_place(queryset, get_parameters.get('place')
        )
    return filter_queryset_by_param(queryset,
                                    get_parameters.get('sort_type', ''),
                                    get_parameters.get('filter_field', ''))
