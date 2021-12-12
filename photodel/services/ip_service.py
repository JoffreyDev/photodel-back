from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError


def get_ip(request):
    """
    Определение ip с помощьбю объекта
    request при отправке запроса пользователем
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение айпи пользователя
    return ip


def get_geoip_city_object(ip):
    """
    Получение обьекта класса библиотеки geoip и возврат
    обьекта местоположения по переданному ip
    """
    try:
        geo = GeoIP2()
        return geo.city(ip)
    except AddressNotFoundError:
        return {"city": 'Minsk'}
