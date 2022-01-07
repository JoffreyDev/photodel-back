from django.contrib import admin
from .models import Profile, VerificationCode, ProCategory, Specialization


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'phone', 'status', 'last_ip', ]


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'email_code', ]


@admin.register(ProCategory)
class ProCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_category', ]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name_spec', ]

