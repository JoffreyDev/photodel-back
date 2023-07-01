from channels.db import database_sync_to_async
from accounts.models import Profile, TeamInvites
from django.db.models import Q, When, Case
from asgiref.sync import sync_to_async
from datetime import timedelta
import json


def create_team_invite(invite_sender, invite_receiver):
    TeamInvites.objects.create(
        invite_sender_id=invite_sender, invite_receiver_id=invite_receiver)
    return True


def update_team_invite_status(data, user):
    """
    Updating film request status
    Args:
        data: data from request
        user: current user
    Returns:
        current response data, status
    """

    invite = TeamInvites.objects.get(id=data['request_id'])
    status = data['status']
    current_status = invite.status
    if current_status == 'AWAITING' and invite.invite_receiver.user == user and status in ['ACCEPTED', 'REJECTED']:
        invite.status = status
        invite.save()
        return {'message': 'Статус успешно изменен!'}, 200
    return {'error': f' У вас нет прав для изменения статуса приглашения'}, 403
