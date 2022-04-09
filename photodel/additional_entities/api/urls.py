from django.urls import path

from .views import CountryViewSet, LanguageViewSet, AdvertisementViewSet, \
    CommonViewSet, CityViewSet, PollViewSet

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
    path('check_city/', CityViewSet.as_view({'get': "check_coordinates"}),
         name='check_coordinates'),
    path('list_polls/', PollViewSet.as_view({'get': "list_poll"}),
         name='list_poll'),
    path('add_answer/', PollViewSet.as_view({'post': "add_answer"}),
         name='add_answer'),
    path('last_comments/', CommonViewSet.as_view({'get': "list_last_comments"}),
         name='list_last_comments'),
]

