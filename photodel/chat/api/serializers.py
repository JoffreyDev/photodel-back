from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from chat.models import Chat, Message

import logging

from film_places.models import FilmRequest

logger = logging.getLogger(__name__)


class ChatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'sender_id', 'receiver_id', )


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('author', 'content', 'chat')


class ChangeFilmRequestSerializer(serializers.Serializer):
    """ Serializer for updating film request status"""

    request_id = serializers.IntegerField()
    filming_status = serializers.ChoiceField(choices=FilmRequest.FILMING_STATUS_CHOICES)

    def validate_request_id(self, request_id):
        film_request = FilmRequest.objects.filter(id=request_id).exists()
        if not film_request:
            raise ValidationError('film request does not exist')
        return request_id
