from geopy.distance import geodesic
from additional_entities.models import Answer


def check_town_use_coords(cities, user_coordinates):
    if not user_coordinates:
        return []
    less_distance = 99999999
    nearest_city = []
    for city in cities:
        distance_diff = geodesic(city.coordinates, user_coordinates).m
        if distance_diff < less_distance:
            less_distance = distance_diff
            nearest_city = city
    return nearest_city


def check_exitst_answer(user, choice):
    user_choice = Answer.objects.filter(profile__user=user, choice=choice)
    if user_choice:
        return True
    return False


