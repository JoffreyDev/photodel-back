from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from chat.api.serializers import ChatCreateSerializer, MessageCreateSerializer
from services.chat_service import is_chat_unique

import logging

logger = logging.getLogger(__name__)


class ChatViewSet(viewsets.ViewSet):
    """
    Класс для представления чата
    """
    permission_classes_by_action = {
        'create_chat': [permissions.IsAuthenticated, ],
        }

    def create_chat(self, request):
        """
        Создание нового чата
        """
        try:
            chat_id = is_chat_unique(request.data.get('sender_id', ''), request.data.get('receiver_id', ''))
            if not chat_id:
                serializer = ChatCreateSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": f'Такой чат уже был создан id={chat_id}'})
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'sender or receiver ids not given'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]