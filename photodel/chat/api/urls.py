from django.urls import path

from chat.api.views import ChatViewSet, ChangeFilmRequestApiView

app_name = 'chat'

urlpatterns = [
    path('create/', ChatViewSet.as_view({"post": "create_chat"})),
    path('update_film_request_status/', ChangeFilmRequestApiView.as_view(), name='update_film_request_status'),
]
