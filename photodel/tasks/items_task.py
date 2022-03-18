from photodel.celery import app
from accounts.models import Profile
from film_places.models import FilmPlaces


@app.task
def task_delete_last_views():
    Profile.objects.update(last_views=0)
    FilmPlaces.objects.update(last_views=0)
