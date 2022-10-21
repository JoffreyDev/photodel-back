from tkinter import Place
from photodel.celery import app
from accounts.models import Profile
from film_places.models import FilmPlaces
from film_places.models import FilmPlacesLike
from services.accounts_service import collect_like


@app.task
def task_delete_last_views():
    Profile.objects.update(last_views=0)
    FilmPlaces.objects.update(last_views=0)


@app.task
def task_update_place_likes():

    def get_likes(self, obj):
        return FilmPlacesLike.objects.filter(place=obj.id).count()

    places_list = FilmPlaces.objects.values_list('pk', flat=True)
    for place in places_list:
        FilmPlaces.objects.filter(pk=place).update(
            likes=get_likes(place))
