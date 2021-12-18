from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterAPIView, ProfileViewSet, VerificationEmailViewSet, \
    ChangePasswordView, CustomTokenObtainPairView, CategoriesProfileViewSet, \
    AlbumViewSet, GalleryViewSet

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(),
         name='register'),
    path('token/', CustomTokenObtainPairView.as_view(),
         name="login"),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

    path('email/send/', VerificationEmailViewSet.as_view({'get': "send_email"}),
         name='send_email'),
    path('email/check/', VerificationEmailViewSet.as_view({'post': "verify_email"}),
         name='verify_email'),

    path('profile/', ProfileViewSet.as_view({'get': "private_profile"}),
         name='private_profile'),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': "public_profile"}),
         name='public_profile'),
    path('profile/update/', ProfileViewSet.as_view({'post': "partial_update"}),
         name='profile_update'),
    path('user/update-password/', ChangePasswordView.as_view({"post": 'update_password_after_reset'}),
         name='update_password_after_reset'),
    path('reset-password-email/', ChangePasswordView.as_view({"post": 'generate_token_for_reset_password'}),
         name='generate_token_for_reset_password'),
    path('profiles/search/', ProfileViewSet.as_view({'get': "search_profiles"}),
         name='search_profiles'),
    path('list_specialization/', CategoriesProfileViewSet.as_view({'get': "list_specialization"}),
         name='list_specialization'),
    path('list_pro_categories/', CategoriesProfileViewSet.as_view({'get': "list_pro_categories"}),
         name='list_pro_categories'),

    path('album/create/', AlbumViewSet.as_view({'post': "create_album"}),
         name='create_album'),
    path('album/list/<int:pk>/', AlbumViewSet.as_view({'get': "list_user_albums"}),
         name='list_user_albums'),
    path('album/list_photos/<int:pk>/', AlbumViewSet.as_view({'get': "list_album_photos"}),
         name='list_album_photos'),

    path('photo/create/', GalleryViewSet.as_view({'post': "create_photo"}),
         name='create_photo'),
    path('photo/<int:pk>/', GalleryViewSet.as_view({'get': "retrieve_photo"}),
         name='retrieve_photo'),
    path('photo/list/<int:pk>/', GalleryViewSet.as_view({'get': "list_photos"}),
         name='list_photos'),
]

