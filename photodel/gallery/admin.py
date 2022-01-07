from django.contrib import admin
from .models import Image, Album, Gallery, GalleryComment, GalleryLike, GalleryFavorite


@admin.register(Image)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['photo', ]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name_album', ]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name_image', 'place_location', 'photo_camera', 'views', 'id', ]


@admin.register(GalleryComment)
class GalleryCommentAdmin(admin.ModelAdmin):
    list_display = ['sender_comment', 'gallery', 'content', 'timestamp', ]


@admin.register(GalleryLike)
class GalleryLikeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'gallery', ]


@admin.register(GalleryFavorite)
class GalleryFavoriteAdmin(admin.ModelAdmin):
    list_display = ['profile', 'gallery', ]