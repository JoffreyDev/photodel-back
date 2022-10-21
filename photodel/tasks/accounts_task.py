from django.template.loader import render_to_string
from additional_entities.models import Advertisement, CustomSettings
from gallery.models import Gallery
from gallery.models import GalleryLike
from services.accounts_service import send_email_to_users, get_name_user
from additional_entities.models import EmailFragment
from photodel.celery import app
from django.conf import settings
from accounts.models import Profile
from services.accounts_service import collect_like
from film_places.models import FilmPlaces
from film_places.models import FilmPlacesLike
from django.utils import timezone
import datetime


@app.task
def task_delete_last_views():
    Profile.objects.update(last_views=0)
    FilmPlaces.objects.update(last_views=0)


# @app.task
# def task_update_place_likes():

#     def get_likes(place):
#         return FilmPlacesLike.objects.filter(place=place).count()

#     places_list = FilmPlaces.objects.values_list('pk', flat=True)
#     for place in places_list:
#         FilmPlaces.objects.filter(pk=place).update(
#             likesStat=get_likes(place))


@app.task
def task_send_email_to_user(email, code):
    title = f'Платформа photodel приветствует вас'
    url = f'{settings.BASE_URL}?email_token={code}'
    login_or_name, profile = get_name_user(email)
    placement_piece = EmailFragment.objects.all().first().verify_email
    html_content = render_to_string('mail_templates/mail.html', {"login": login_or_name,
                                                                 "placement_piece": placement_piece,
                                                                 "fragment": url})
    return send_email_to_users(title, [email], html_content)


@app.task
def task_send_reset_password_to_email(email, code):
    title = 'Платформа photodel.by приветствует вас'
    url = f'{settings.BASE_URL}?reset_token={code}'
    login_or_name, profile = get_name_user(email)
    placement_piece = EmailFragment.objects.all().first().reset_password
    html_content = render_to_string('mail_templates/mail.html', {"login": login_or_name,
                                                                 "placement_piece": placement_piece,
                                                                 "fragment": url})
    return send_email_to_users(title, [email], html_content)


@app.task
def task_send_email_to_verify_not_auth_request(email, code):
    title = f'Платформа photodel приветствует вас'
    login_or_name, profile = get_name_user(email)
    placement_piece = EmailFragment.objects.all(
    ).first().verify_email_for_not_auth_request
    html_content = render_to_string('mail_templates/mail.html', {"login": login_or_name,
                                                                 "placement_piece": placement_piece,
                                                                 "fragment": code})
    return send_email_to_users(title, [email], html_content)


# @app.task
# def task_update_current_ad():
#     current_ad = CustomSettings.objects.all().first().current_ad
#     ads_list = sorted(Advertisement.objects.filter(
#         status=1).values_list('pk', flat=True))

#     if current_ad == ads_list[-1]:
#         CustomSettings.objects.update(
#             current_ad=ads_list[0])
#         return

#     if current_ad != ads_list[-1]:
#         index = ads_list.index(current_ad)
#         CustomSettings.objects.update(
#             current_ad=ads_list[index + 1])
#         return


# @app.task
# def task_update_profile_likes():
#     profiles_list = Profile.objects.values_list('pk', flat=True)
#     for profile in profiles_list:
#         Profile.objects.filter(pk=profile).update(likes=collect_like(profile))


# @app.task
# def task_update_photos_likes():
#     def get_likes(gallery):
#         return GalleryLike.objects.filter(gallery=gallery).count()

#     photos_list = Gallery.objects.values_list('pk', flat=True)
#     for gallery in photos_list:
#         Gallery.objects.filter(pk=gallery).update(
#             likesStat=get_likes(gallery))


# @app.task
# def check_ads_dates():
#     ads_list = Advertisement.objects.values_list('pk', flat=True)
#     for ad in ads_list:
#         if Advertisement.objects.filter(pk=ad).all().first().start <= timezone.now() and Advertisement.objects.filter(pk=ad).all().first().end >= timezone.now():
#             Advertisement.objects.filter(pk=ad).update(status=1)
#         else:
#             Advertisement.objects.filter(pk=ad).update(status=0)


# @app.task
# def reset_temp_location():
#     profiles = Profile.objects.values_list('pk', flat=True)
#     for profile in profiles:
#         if Profile.objects.filter(pk=profile).all().first().date_stay_end and Profile.objects.filter(pk=profile).all().first().date_stay_end <= timezone.now():
#             Profile.objects.filter(pk=profile).update(location_now=None)
#             Profile.objects.filter(pk=profile).update(string_location_now=None)
#             Profile.objects.filter(pk=profile).update(date_stay_start=None)
#             Profile.objects.filter(pk=profile).update(date_stay_end=None)
#             Profile.objects.filter(pk=profile).update(message='')
