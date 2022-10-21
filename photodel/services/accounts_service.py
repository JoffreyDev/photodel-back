from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User, AnonymousUser
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers
from django.contrib.gis.geos import Point
from accounts.models import VerificationCode, Profile
from gallery.models import GalleryLike, GalleryFavorite, PhotoSessionLike, \
    PhotoSessionFavorite, PhotoSessionComment, GalleryComment
from film_places.models import FilmPlacesLike, FilmPlacesFavorite, FilmPlacesComment
from additional_entities.models import BanWord
from smtplib import SMTPException
from django.utils import timezone
import random
from django.db.models.functions import Lower


def custom_paginator(queryset, request):
    """
    Кастомный пагинатор страниц
    """
    try:
        page = request.GET.get('page')
        count_positions = int(request.GET.get('count_positions', 8))
        paginator = Paginator(queryset, count_positions)
        return paginator.page(page)
    except PageNotAnInteger:
        return queryset[:10]
    except ValueError:
        return []
    except EmptyPage:
        return []


def is_valid_email(email):
    """
    Функция проверки валидности емейла
    """
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def send_email_to_users(title, to_email, html_content, from_email=settings.EMAIL_HOST_USER):
    """
    Отправка одного мыла
    """
    try:
        if send_mail(
            # title:
            title,
            # message:
            None,
            # from:
            f'photodel <{from_email}>',
            # to:
            to_email,
            html_message=html_content,
            fail_silently=False,
        ):

            return True

        return False
    except SMTPException:
        return False
    except Exception as e:
        return False


def check_email_verification_code(verification_code):
    """
    Проверка соответствия введного кода с кодом в бд
    Если успешно, флаг верифицирован ли емейл меняется на True
    :return:
    """
    code = VerificationCode.objects.filter(email_code=verification_code).last()
    profile = code.profile_id
    if code.email_code == verification_code:
        profile.email_verify = True
        profile.save()
        return True
    return False


def return_user_use_reset_token(token):
    """
    Проверка соответствия введного кода с кодом в бд
    Если успешно, флаг верифицирован ли емейл меняется на True
    :return:
    """
    code = VerificationCode.objects.filter(password_reset_token=token).last()
    if code.password_reset_token == token:
        return code.profile_id.user
    return AnonymousUser


def update_or_create_verification_token(profile, code, type_action):
    """
    Функция проверяет есть ли email в таблице VerificationCode
    если есть - обновляет код, если нет создает новую запись
    """
    try:
        instance = VerificationCode.objects.get(profile_id=profile)
        if type_action == 'reset':
            instance.password_reset_token = code
            instance.save()
        elif type_action == 'verify':
            instance.email_code = code
            instance.save()
    except VerificationCode.DoesNotExist:
        if type_action == 'reset':
            VerificationCode.objects.create(
                profile_id=profile, password_reset_token=code)
        else:
            VerificationCode.objects.create(
                profile_id=profile, email_code=code)


def create_random_code(count_number):
    """
    Функция создания рандомного пароля
    """
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return "".join([random.choice(chars) for _ in range(count_number)])


def get_name_user(email):
    """
    Получение имени пользователя или логина пользовтаеля
    если имени не указано
    """
    profile = Profile.objects.filter(email=email).first()
    if profile:
        return profile.name, profile if profile.name else profile.user.username
    return None, None


def check_is_unique_email(email, user):
    """
    Проверка на уникальность емейла
    """
    profile = Profile.objects.filter(email=email).exclude(user=user)
    if email and profile.exists():
        raise serializers.ValidationError("Такой емейл уже существует")


def convert_string_coordinates_to_point_obj(coordinates):
    """
    Функция конвертации координат в Point объект
    КоОрдинаты могут быть двух типов SRID=4326;POINT (27.449901 53.903557) и 27.449901 53.903557
    Если переданные координаты не кооректны для одно из типов, то возврващается координаты г.Москвы
    """
    try:
        split_coord = coordinates.split()
        if 'SRID' in coordinates:
            first, second = split_coord[1][1:], split_coord[2][:-1]
        else:
            first, second = split_coord[0], split_coord[1]
        pnt = Point(float(first), float(second))
        return pnt
    except Exception:
        return Point(55.753220, 37.622513)


def check_profile_location(queryset):
    """
    Функция провери местонахождения профиля
    Если текущее время больше date_stay_end, значит координаты берутся с location_now
    иначе координаты берутся location
    """
    if queryset.date_stay_end and queryset.date_stay_end > timezone.localtime():
        return queryset.location_now
    return queryset.location


def collect_favorite(user):
    """
    Фотки, места фотосессии пользователя, которые добавили к себе в избранное другие пользователи
    """
    places_count = FilmPlacesFavorite.objects.filter(
        place__profile__user=user).count()
    galleries_count = GalleryFavorite.objects.filter(
        gallery__profile__user=user).count()
    photo_session_count = PhotoSessionFavorite.objects.filter(
        photo_session__profile__user=user).count()
    return places_count + galleries_count + photo_session_count


def collect_like(user):
    """
    Фотки, места фотосессии пользователя, на которые поставили лайки другие пользователи
    """
    places_count = FilmPlacesLike.objects.filter(
        place__profile__user=user).count()
    galleries_count = GalleryLike.objects.filter(
        gallery__profile__user=user).count()
    photo_session_count = PhotoSessionLike.objects.filter(
        photo_session__profile__user=user).count()
    return places_count + galleries_count + photo_session_count


def collect_comment(user):
    """
    Фотки, места фотосессии пользователя, на которые поставили лайки другие пользователи
    """
    places_count = FilmPlacesComment.objects.filter(
        place__profile__user=user).count()
    galleries_count = GalleryComment.objects.filter(
        gallery__profile__user=user).count()
    photo_session_count = PhotoSessionComment.objects.filter(
        photo_session__profile__user=user).count()
    return places_count + galleries_count + photo_session_count


def check_obscene_word_in_content(content):
    ban_words = BanWord.objects.values('word')
    for word in ban_words:
        if word.get('word') in content:
            return True
    return False


def filter_queryset_by_param(queryset, sort_type, filter_field):
    """
    Функция сортировки queryset
    Фильтрация по просмотрам или последним просматрам за неделю,
    каждую неделю поле last_views сбрасывается до 0
    Или фильтрация по полю в queryset
    sort_type = ничего, если по возрастанию
              = знак -, если по убыванию
    filter_field = сооотствует полю в модели, которую необходимо отфильтровать
    Пример: Модель Gallery фильтр по алфавиту, поле название.
    ?sort_type=&filter_field=name_image
    """
    try:
        if not filter_field:
            return queryset
        return queryset.order_by(f'{sort_type}{filter_field}')
    except Exception as e:
        print(e)
        return queryset
