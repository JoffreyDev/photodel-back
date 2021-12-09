from django.contrib import admin
from .models import Profile, VerificationCode


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'phone', 'status', 'last_ip', ]


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'email_code', ]
