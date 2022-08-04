from geopy.distance import geodesic
from additional_entities.models import Answer, Choice


def check_town_use_coords(cities, user_coordinates):
    """
    Функция нахождения самого близкого города к пользователю
    """
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
    """
    Проверка, отвечал ли, пользователь на опрос
    """

    choice = Choice.objects.get(id=choice)
    user_choice = Answer.objects.filter(profile__user=user).first()
    if not user_choice:
        return False
    print(user_choice.choice.question.id)
    print(choice.question.id)
    if user_choice.choice.question == choice.question:
        return True

    if user_choice:
        return True
    return False


