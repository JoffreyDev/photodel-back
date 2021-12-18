from django.contrib import admin
from .models import EmailFragment, CustomSettings, Country


admin.site.register(EmailFragment)
admin.site.register(CustomSettings)


@admin.register(Country)
class CountryImagesAdmin(admin.ModelAdmin):
    list_display = ['name_country', ]