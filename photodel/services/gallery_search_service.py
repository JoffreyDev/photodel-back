from django.db.models import Q
from itertools import chain
from django.contrib.gis.measure import D
from services.gallery_service import filter_queryset_by_param
from services.accounts_service import convert_string_coordinates_to_point_obj


def filter_gallery_by_distance(queryset, user_coordinates, distance):
    if not (user_coordinates or distance):
        return queryset
    user_coordinates = convert_string_coordinates_to_point_obj(user_coordinates)
    profiles = queryset.filter(Q(place_location__distance_lte=(user_coordinates, D(m=distance))))\
        .select_related('gallery_image', 'profile')
    return profiles


def filter_gallery_by_category(queryset, category):
    if not category:
        return queryset
    return queryset.filter(category__name_spec=category).select_related('gallery_image', 'profile')


def filter_gallery_by_words(queryset, search_words):
    search_words = search_words.split()
    if not search_words:
        return queryset
    if len(search_words) == 1:
        search_words = search_words[0]
        queryset = queryset.filter(
            (Q(name_image__icontains=search_words) |
             Q(description__icontains=search_words)) &
            Q(is_hidden=False)).select_related('gallery_image', 'profile')
        return queryset
    else:
        result_list = []
        for field in search_words:
            gallery = queryset.filter(
                (Q(name_image__icontains=field) |
                 Q(description__icontains=field)) &
                Q(is_hidden=False)).select_related('gallery_image', 'profile')
            if gallery:
                result_list += chain(gallery)
        return list(set(result_list))


def filter_gallery_queryset(queryset, get_parameters):
    queryset = filter_gallery_by_category(queryset,
                                          get_parameters.get('category', ''))
    queryset = filter_gallery_by_distance(queryset,
                                          get_parameters.get('user_coordinates'),
                                          get_parameters.get('distance'))
    filter_queryset = filter_gallery_by_words(queryset, get_parameters.get('search_words', ''))
    return filter_queryset_by_param(filter_queryset,
                                    get_parameters.get('sort_type', ''),
                                    get_parameters.get('filter_field', ''))