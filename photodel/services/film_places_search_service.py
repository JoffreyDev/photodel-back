from django.db.models import Q
from itertools import chain
from django.contrib.gis.measure import D
from services.gallery_service import filter_queryset_by_param
from services.accounts_service import convert_string_coordinates_to_point_obj


def filter_film_places_by_distance(queryset, user_coordinates, distance):
    if not (user_coordinates or distance):
        return queryset
    user_coordinates = convert_string_coordinates_to_point_obj(user_coordinates)
    profiles = queryset.filter(Q(place_location__distance_lte=(user_coordinates, D(m=distance)))) \
        .select_related('profile').prefetch_related('place_image')
    return profiles


def filter_film_places_by_category(queryset, category):
    return queryset.filter(category__name_category=category).select_related('profile').prefetch_related('place_image')


def filter_film_places_by_words(queryset, search_words):
    search_words = search_words.split()
    if not search_words:
        return queryset
    if len(search_words) == 1:
        search_words = search_words[0]
        queryset = queryset.filter(
            (Q(name_place__icontains=search_words) |
             Q(description__icontains=search_words)) &
            Q(is_hidden=False)).select_related('profile').prefetch_related('place_image')
        return queryset
    else:
        result_list = []
        for field in search_words:
            place = queryset.filter(
                (Q(name_place__icontains=field) |
                 Q(description__icontains=field)) &
                Q(is_hidden=False)).select_related('profile').prefetch_related('place_image')
            if place:
                result_list += chain(place)
        return list(set(result_list))


def filter_film_places_queryset(queryset, get_parameters):
    queryset = filter_film_places_by_category(queryset,
                                          get_parameters.get('category', ''))
    queryset = filter_film_places_by_distance(queryset,
                                          get_parameters.get('user_coordinates'),
                                          get_parameters.get('distance'))
    filter_queryset = filter_film_places_by_words(queryset, get_parameters.get('search_words', ''))
    print(filter_queryset)
    return filter_queryset_by_param(filter_queryset,
                                    get_parameters.get('sort_type', ''),
                                    get_parameters.get('filter_field', ''))