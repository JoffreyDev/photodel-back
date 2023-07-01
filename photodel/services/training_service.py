from channels.db import database_sync_to_async
from trainings.models import TrainingsRequest
from django.db.models import Q, When, Case
from asgiref.sync import sync_to_async
from datetime import timedelta
import json


def update_training_request_status(data, user):
    """
    Updating film request status
    Args:
        data: data from request
        user: current user
    Returns:
        current response data, status
    """

    request = TrainingsRequest.objects.get(id=data['request_id'])
    status = data['status']
    current_status = request.status
    if current_status == 'AWAITING' and (user in request.training.training_orgs.all() or user == request.training.profile.user) and status in ['ACCEPTED', 'REJECTED']:
        request.status = status
        request.save()
        return {'message': 'Статус успешно изменен!'}, 200
    return {'error': f' У вас нет прав для изменения статуса приглашения'}, 403
