from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import Profile
from django.utils import timezone
from rest_framework_simplejwt.exceptions import InvalidToken
from oauth2_provider.models import AccessToken


class UserVisit:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            jwt_authenticator = JWTAuthentication()
            header = jwt_authenticator.get_header(request)
            if not header:
                return self.get_response(request)

            jwt_token = jwt_authenticator.get_raw_token(header)
            if len(jwt_token) == 30:
                self.get_social_user(jwt_token)
                return self.get_response(request)

            jwt_payload = jwt_authenticator.authenticate(request)
            if jwt_payload is not None:
                user, token = jwt_payload
                profile = Profile.objects.get(user=user)
                profile.last_date_in = timezone.localtime()
                profile.save()
            return self.get_response(request)
        except TypeError:
            return self.get_response(request)
        except InvalidToken:
            return self.get_response(request)
        except Profile.DoesNotExist:
            return self.get_response(request)

    def get_social_user(self, token):
        token = AccessToken.objects.filter(token=token.decode('utf-8')).first()
        if token:
            profile = Profile.objects.get(user=token.user)
            profile.last_date_in = timezone.localtime()
            profile.save()