from film_places.models import FilmRequest


def update_film_request_status(data, user):
    """
    Updating film request status
    Args:
        data: data from request
        user: current user
    Returns:
        current response data, status
    """

    film_request = FilmRequest.objects.get(id=data['request_id'])
    status = data['filming_status']
    current_status = film_request.filming_status
    if current_status == 'NEW' and film_request.receiver_profile.user == user and status in ['ACCEPTED', 'REJECTED']:
        film_request.filming_status = status
        film_request.save()
        return {'message': 'Статус запроса успешно изменен!'}, 200
    if current_status == 'ACCEPTED' and film_request.profile.user == user and status in ['COMPLETED', 'UNCOMPLETED']:
        film_request.filming_status = status
        film_request.save()
        return {'message': 'Статус запроса успешно изменен!'}, 200
    return {'error': f'You haven`t permissions to change status'}, 403
