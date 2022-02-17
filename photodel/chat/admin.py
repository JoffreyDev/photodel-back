from django.contrib import admin
from .models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['sender_id', 'receiver_id', 'id', ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'chat', 'status_read', 'id', ]