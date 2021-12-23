from django.contrib import admin
from .models import EmailFragment, CustomSettings, Country, Language


admin.site.register(EmailFragment)
admin.site.register(CustomSettings)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name_country', ]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name_language', ]