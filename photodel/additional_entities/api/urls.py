from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CountryViewSet

app_name = 'additional_entities'

urlpatterns = [
    path('list_country/', CountryViewSet.as_view({'get': "list_country"}),
         name='list_country'),
]

