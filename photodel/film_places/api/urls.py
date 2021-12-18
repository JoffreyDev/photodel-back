from django.urls import path

from .views import FilmPlacesViewSet, CategoryFilmPlacesViewSet

app_name = 'film_places'

urlpatterns = [
    path('create/', FilmPlacesViewSet.as_view({'post': "create_place"}),
         name='create_place'),
    path('list/', CategoryFilmPlacesViewSet.as_view({'get': "list_category"}),
         name='list_category'),
]

