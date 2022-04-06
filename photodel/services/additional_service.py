from geopy.distance import geodesic


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
