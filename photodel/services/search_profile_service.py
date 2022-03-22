from django.db.models import Q
from django.contrib.gis.measure import D
from services.accounts_service import convert_string_coordinates_to_point_obj
from django.utils import timezone
from itertools import chain


def filter_by_category_and_spec(filter_queryset, name_spec, name_category):
    """
    Фильтрация категории и специализации профиля, если паратры были переданы
    """
    if name_category:
        filter_queryset = filter_queryset.filter(type_pro__name_category=name_category)
    if name_spec:
        filter_queryset = filter_queryset.filter(spec_model_or_photographer__name_spec=name_spec)
    return filter_queryset


def filter_by_initials(profiles, search_words):
    """
    Фильтрация имени и фамилии профиля
    Фильтруется в зависимости от количества слов в гет параметры search_words
    """
    search_words = search_words.split()
    if not search_words:
        return profiles
    if len(search_words) == 1:
        search_words = search_words[0]
        queryset = profiles.filter(Q(name__icontains=search_words) | Q(surname__icontains=search_words))
        return queryset
    else:
        queryset = []
        for field in search_words:
            profile = profiles.filter(Q(name__icontains=field) | Q(surname__icontains=field))
            if profile:
                queryset += chain(profile)
        return list(set(queryset))


def filter_by_distance(profiles, user_coordinates, distance):
    """
    Филтррация по радиусу
    """
    if not (user_coordinates or distance):
        return profiles
    user_coordinates = convert_string_coordinates_to_point_obj(user_coordinates)
    profiles = profiles.filter(Q(date_stay_end__gte=timezone.localtime()) &
                               Q(location_now__distance_lte=(user_coordinates, D(m=distance))) |
                               (Q(date_stay_end__lte=timezone.localtime()) | Q(date_stay_end=''))
                               & Q(location__distance_lte=(user_coordinates, D(m=distance)))
                               )
    return profiles


def filter_by_all_parameters(profiles, request_data):
    """
    Филтррация по всем переданным параметрам из переменной request_data
    """
    by_categories = filter_by_category_and_spec(profiles,
                                                request_data.get('name_spec', ''),
                                                request_data.get('name_category', ''))
    by_distance = filter_by_distance(by_categories,
                                     request_data.get('coordinates', ''),
                                     request_data.get('distance', ''))
    by_initials = filter_by_initials(by_distance,
                                     request_data.get('search_words', ''))
    return by_initials
