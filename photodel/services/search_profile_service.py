from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q
from geopy.distance import geodesic
from django.utils import timezone


def filter_by_distance(profiles, user_coordinates, distance):
    """
    Фильтрация по радиусу
    Если у пользователя есть крайний срок временной геолакции
    и он больше текущего времени,
    то берется временная геолакация, иначе постоянная
    """
    if not (user_coordinates or distance):
        return profiles
    filter_queryset = []
    try:
        for query in profiles:
            if query.date_stay_end and query.date_stay_end > timezone.localtime():
                distance_diff = geodesic(query.location_now, user_coordinates).m
            else:
                distance_diff = geodesic(query.location, user_coordinates).m

            if float(distance) > float(distance_diff):
                filter_queryset.append(query.id)
        return profiles.filter(id__in=filter_queryset)
    except ValueError:
        return []


def filter_by_category_and_spec(filter_queryset, name_spec, name_category):
    """
    Фильтрация категории и специализации профиля, если паратры были переданы
    """
    if name_category:
        filter_queryset = filter_queryset.filter(type_pro__name_category=name_category)
    if name_spec:
        filter_queryset = filter_queryset.filter(spec_model_or_photographer__name_spec=name_spec)
    return filter_queryset


def filter_by_ready_status(filter_queryset, ready_status):
    """
    Фильтрация по статусу готовности
    """
    if ready_status:
        filter_queryset = filter_queryset.filter(ready_status=ready_status)
    return filter_queryset


def filter_by_address(filter_queryset, address):
    """
    Фильтрация по статусу готовности
    """
    address = address.split()
    if not address:
        return filter_queryset
    if len(address) == 1:
        address = address[0]
        queryset = filter_queryset.filter(Q(string_location__icontains=address))
        return queryset
    else:
        search_vector = SearchVector("string_location")
        search_query = SearchQuery(" | ".join(address), search_type="raw")
        return filter_queryset.annotate(search=search_vector).filter(search=search_query)


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
        search_vector = SearchVector("name", "surname")
        search_query = SearchQuery(" | ".join(search_words), search_type="raw")
        return profiles.annotate(search=search_vector).filter(search=search_query)


def filter_by_all_parameters(profiles, request_data):
    """
    Филтррация по всем переданным параметрам из переменной request_data
    """
    by_categories = filter_by_category_and_spec(profiles,
                                                request_data.get('name_spec', ''),
                                                request_data.get('name_category', ''))
    by_ready_status = filter_by_ready_status(by_categories,
                                             request_data.get('ready_status', ''))
    by_address = filter_by_address(by_ready_status,
                                   request_data.get('address', ''))
    by_distance = filter_by_distance(by_address,
                                     request_data.get('user_coords', ''),
                                     request_data.get('distance', ''))
    by_initials = filter_by_initials(by_distance,
                                     request_data.get('search_words', ''))
    return by_initials
