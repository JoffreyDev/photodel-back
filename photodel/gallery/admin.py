from django.contrib import admin
from .models import Image, Album, Gallery, GalleryComment, GalleryLike, GalleryFavorite, \
    PhotoSession, PhotoSessionComment, PhotoSessionLike, PhotoSessionFavorite, Review


@admin.register(Image)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'profile', ]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name_album', 'id', ]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name_image', 'place_location',
                    'photo_camera', 'views', 'id', ]


@admin.register(GalleryComment)
class GalleryCommentAdmin(admin.ModelAdmin):
    list_display = ['sender_comment', 'gallery', 'content', 'timestamp', ]


@admin.register(GalleryLike)
class GalleryLikeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'gallery', ]


@admin.register(GalleryFavorite)
class GalleryFavoriteAdmin(admin.ModelAdmin):
    list_display = ['profile', 'gallery', ]


@admin.register(PhotoSession)
class PhotoSessionAdmin(admin.ModelAdmin):
    list_display = ['session_name', 'session_location',
                    'session_date', 'profile', 'id', ]


@admin.register(PhotoSessionComment)
class PhotoSessionCommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'timestamp',
                    'sender_comment', 'photo_session', ]


@admin.register(PhotoSessionLike)
class PhotoSessionLikeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'photo_session', ]


@admin.register(PhotoSessionFavorite)
class PhotoSessionFavoriteAdmin(admin.ModelAdmin):
    list_display = ['profile', 'photo_session', ]


@admin.register(Review)
class PhotoSessionFavoriteAdmin(admin.ModelAdmin):
    list_display = ['content', ]
