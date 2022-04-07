from rest_framework import serializers
from chat.models import Chat, Message

import logging

logger = logging.getLogger(__name__)


class ChatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'sender_id', 'receiver_id', )


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('author', 'content', 'chat')

