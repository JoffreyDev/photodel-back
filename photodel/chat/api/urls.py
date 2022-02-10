from django.urls import path

from chat.api.views import ChatViewSet

app_name = 'chat'

urlpatterns = [
    path('create/', ChatViewSet.as_view({"post": "create_chat"})),
]