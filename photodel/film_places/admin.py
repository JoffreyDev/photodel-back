from django.contrib import admin
from .models import FilmPlaces, CategoryFilmPlaces, FilmPlacesComment, FilmPlacesLike, FilmPlacesFavorite


@admin.register(FilmPlaces)
class FilmPlacesAdmin(admin.ModelAdmin):
    list_display = ['profile', 'rel_object', 'id', ]


@admin.register(CategoryFilmPlaces)
class CategoryFilmPlacesAdmin(admin.ModelAdmin):
    list_display = ['name_category', ]


@admin.register(FilmPlacesComment)
class FilmPlacesCommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'timestamp', 'sender_comment', 'place', ]


@admin.register(FilmPlacesLike)
class FilmPlacesLikeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'place', ]


@admin.register(FilmPlacesFavorite)
class FilmPlacesFavoriteAdmin(admin.ModelAdmin):
    list_display = ['profile', 'place', ]