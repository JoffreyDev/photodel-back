from django.urls import path

from .views import CountryViewSet, LanguageViewSet, AdvertisementViewSet, CommonViewSet, CityViewSet

app_name = 'additional_entities'

urlpatterns = [
    path('list_country/', CountryViewSet.as_view({'get': "list_country"}),
         name='list_country'),
    path('list_language/', LanguageViewSet.as_view({'get': "list_language"}),
         name='list_language'),
    path('list_advertisement/', AdvertisementViewSet.as_view({'get': "list_advertisement"}),
         name='list_advertisement'),
    path('add_click_to_advertisement/<int:pk>/', AdvertisementViewSet.as_view({'get': "add_click_to_advertisement"}),
         name='add_click_to_advertisement'),
    path('list_city/', CityViewSet.as_view({'get': "list_city"}),
         name='list_city'),
    path('last_comments/', CommonViewSet.as_view({'get': "list_last_comments"}),
         name='list_last_comments'),
]

