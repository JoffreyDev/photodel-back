from django.contrib import admin
from .models import EmailFragment, CustomSettings


admin.site.register(EmailFragment)
admin.site.register(CustomSettings)
