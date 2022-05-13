import logging

from rest_framework import status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.api.serializers import ChatCreateSerializer, MessageCreateSerializer, ChangeFilmRequestSerializer
from chat.api.services import update_film_request_status
from services.chat_service import is_chat_unique


logger = logging.getLogger(__name__)


class ChangeFilmRequestApiView(APIView):
    """ Api view for changing status of film request """

    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        serializer = ChangeFilmRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        response = update_film_request_status(data=serializer_data, user=request.user)
        return Response(*response)


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
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": f'Такой чат уже был создан id={chat_id}'})
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": 'sender or receiver ids not given'})

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
