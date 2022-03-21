from django.contrib import admin
from .models import EmailFragment, CustomSettings, Country, Language, Advertisement, BanWord


admin.site.register(EmailFragment)
admin.site.register(CustomSettings)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name_country', ]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name_language', ]


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['ad_title', 'ad_link', ]


@admin.register(BanWord)
class BanWordAdmin(admin.ModelAdmin):
    list_display = ['word', ]


