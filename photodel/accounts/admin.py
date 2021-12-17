from django.contrib import admin
from .models import Profile, VerificationCode, ProCategory, Specialization, GalleryImages, Album, Gallery


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'phone', 'status', 'last_ip', ]


@admin.register(GalleryImages)
class GalleryImagesAdmin(admin.ModelAdmin):
    list_display = ['photo', ]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name_album', ]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name_image', 'place_location', 'photo_camera', 'views', 'id', ]


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'email_code', ]


@admin.register(ProCategory)
class ProCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_category', ]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name_spec', 'type_model', ]
