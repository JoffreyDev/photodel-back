from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterAPIView, ProfileViewSet, VerificationEmailViewSet, \
    ChangePasswordView, CustomTokenObtainPairView, CategoriesProfileViewSet, \
    ProfileFavoriteViewSet, ProfileLikeViewSet, ProfileCommentViewSet

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
    path('profile/list/', ProfileViewSet.as_view({'get': "list_profiles"}),
         name='list_profiles'),
    path('profile/popular/', ProfileViewSet.as_view({'get': "popular_profiles"}),
         name='popular_profiles'),
    path('user/update-password/', ChangePasswordView.as_view({"post": 'update_password_after_reset'}),
         name='update_password_after_reset'),
    path('reset-password-email/', ChangePasswordView.as_view({"post": 'generate_token_for_reset_password'}),
         name='generate_token_for_reset_password'),
    path('profile/like/create/', ProfileLikeViewSet.as_view({'post': "create_like"}),
         name='profile_create_like'),
    path('profile/like/delete/<int:pk>/', ProfileLikeViewSet.as_view({'delete': "delete_like"}),
         name='profile_delete_like'),
    path('profile/favorite/list/<int:pk>/', ProfileFavoriteViewSet.as_view({'get': "list_favorite"}),
         name='profile_list_favorite'),
    path('profile/favorite/create/', ProfileFavoriteViewSet.as_view({'post': "create_favorite"}),
         name='profile_create_favorite'),
    path('profile/favorite/delete/', ProfileFavoriteViewSet.as_view({'post': "delete_favorite"}),
         name='profile_delete_favorite'),
    path('profile/comment/list/<int:pk>/', ProfileCommentViewSet.as_view({'get': "list_comments"}),
         name='profile_list_comments'),
    path('profile/comment/create/', ProfileCommentViewSet.as_view({'post': "create_comment"}),
         name='profile_create_comment'),

    path('list_specialization/', CategoriesProfileViewSet.as_view({'get': "list_specialization"}),
         name='list_specialization'),
    path('list_pro_categories/', CategoriesProfileViewSet.as_view({'get': "list_pro_categories"}),
         name='list_pro_categories'),

]

