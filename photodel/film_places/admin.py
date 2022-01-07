from django.contrib import admin
from .models import FilmPlaces, Favorite, CategoryFilmPlaces


@admin.register(FilmPlaces)
class FilmPlacesAdmin(admin.ModelAdmin):
    list_display = ['profile', 'rel_object', ]


@admin.register(CategoryFilmPlaces)
class CategoryFilmPlacesAdmin(admin.ModelAdmin):
    list_display = ['name_category', ]