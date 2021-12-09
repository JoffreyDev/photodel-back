from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import RegisterAPIView, ProfileViewSet, VerificationEmailViewSet, ChangePasswordView
from .serializers import CustomJWTSerializer

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(),
         name='register'),
    path('token/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer),
         name="login"),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

    path('email/send/', VerificationEmailViewSet.as_view({'get': "send_email"}),
         name='send_email'),
    path('email/check/', VerificationEmailViewSet.as_view({'post': "verify_email"}),
         name='verify_email'),

    path('profile/update/', ProfileViewSet.as_view({'post': "partial_update"}),
         name='profile_update'),
    path('update-password/', ChangePasswordView.as_view({"post": 'update_password'}),
         name='update_password'),
    path('reset-password-email/', ChangePasswordView.as_view({"post": 'set_generate_password_use_email'}),
         name='reset_password_email'),
]

