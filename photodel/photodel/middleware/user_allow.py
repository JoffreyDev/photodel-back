from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import Profile
from django.utils import timezone
from rest_framework_simplejwt.exceptions import InvalidToken
from services.ip_service import get_ip
from django.core.exceptions import PermissionDenied


class UserVisit:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allow_urls = ['/api/accounts/email/check/',
                           '/api/accounts/email/send/',
                           '/api/accounts/reset-password-email/',
                           ]

    def __call__(self, request):
        try:
            jwt_authenticator = JWTAuthentication()
            jwt_payload = jwt_authenticator.authenticate(request)
            if jwt_payload is not None:
                user, token = jwt_payload
                profile = Profile.objects.get(user=user)
                if not profile.email_verify and request.path not in self.allow_urls:
                    raise PermissionDenied
                profile.last_date_in = timezone.localtime()
                profile.last_ip = get_ip(request)
                profile.save()
            return self.get_response(request)
        except TypeError:
            return self.get_response(request)
        except InvalidToken:
            return self.get_response(request)
        except Profile.DoesNotExist:
            return self.get_response(request)