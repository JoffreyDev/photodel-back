from django.db.models import Count, Case, When
from film_places.models import FilmPlaces, FilmPlacesLike, NotAuthFilmRequest
from additional_entities.models import CustomSettings
from datetime import timedelta
from django.utils import timezone


def get_popular_places(category):
    """
    Функция сбора популярных мест для съемок на основе лайков,
    чем больше лайков, тем выше место в слайдере и фильтрации их по названию категории
    Если мест получается меньще 10, то идет добавление рандомных мест
    """
    list_best_places = [place_id.get('place') for place_id in FilmPlacesLike.objects.values('place')
        .annotate(dcount=Count('place')).order_by('-dcount').values('place')]
    if category:
        places = list(FilmPlaces.objects.filter(id__in=list_best_places, category__name_category=category) \
                     .order_by(Case(*[When(id=n, then=i) for i, n in enumerate(list_best_places)], ))[:10])
        return places
    else:
        places = list(FilmPlaces.objects.filter(id__in=list_best_places) \
                     .order_by(Case(*[When(id=n, then=i) for i, n in enumerate(list_best_places)], ))[:10])
    if len(places) < 10:
        places += list(FilmPlaces.objects.exclude(id__in=list_best_places))
    return places


def update_not_auth_code(request_id, code):
    """
    Функция дли сохрание кода подтвреждения при запросе как неавторизованный пользователь
    """
    try:
        request = NotAuthFilmRequest.objects.get(id=request_id)
        request.email_code = code
        request.save()
    except NotAuthFilmRequest.DoesNotExist:
        return False
    except ValueError:
        return False


def validate_confirmation_code(email, code):
    """
    Проверка кода на корректость путем фильтрации таблицы по емейлу
    """
    if not email or not code:
        return False
    request = NotAuthFilmRequest.objects.filter(email=email).last()
    if not request:
        return False
    if request.email_code == code:
        request.email_verify = True
        request.save()
        return True
    return False


def check_user_allow_give_request(email):
    """
    Функцмя проверки возможности запроса как неавторизованный пользователь
    Если от последнего запроса прошло больше дней,
    чем в настройках, запрос можно сделать
    """
    site_settings = CustomSettings.objects.all().first()
    request = NotAuthFilmRequest.objects.filter(email=email).last()
    if not request:
        return True
    if request.was_added + timedelta(hours=3, days=site_settings.days_request_to_not_auth_user) < timezone.localtime():
        return True
    return False


