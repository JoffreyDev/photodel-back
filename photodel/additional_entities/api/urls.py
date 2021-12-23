from django.urls import path

from .views import CountryViewSet, LanguageViewSet

app_name = 'additional_entities'

urlpatterns = [
    path('list_country/', CountryViewSet.as_view({'get': "list_country"}),
         name='list_country'),
    path('list_language/', LanguageViewSet.as_view({'get': "list_language"}),
         name='list_language'),
]

