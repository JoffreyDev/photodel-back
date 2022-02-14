from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User, AnonymousUser
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers
from django.contrib.gis.geos import Point
from accounts.models import VerificationCode, Profile
from smtplib import SMTPException
from django.utils import timezone
import random



def custom_paginator(queryset, request):
    """
    Кастомный пагинатор страниц
    """
    paginator = Paginator(queryset, settings.PAGE_SIZE)
    page = request.GET.get('page')
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
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
            VerificationCode.objects.create(profile_id=profile, password_reset_token=code)
        else:
            VerificationCode.objects.create(profile_id=profile, email_code=code)


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
