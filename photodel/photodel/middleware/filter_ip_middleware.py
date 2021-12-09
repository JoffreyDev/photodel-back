from django.core.exceptions import PermissionDenied
from additional_entities.models import BlackList


class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_ips = []
        block = BlackList.objects.all()
        for i in block:
            blocked_ips.append(i.user_ip)
        ip = request.META.get('REMOTE_ADDR')
        if ip in blocked_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response