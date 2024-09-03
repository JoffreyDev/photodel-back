from django.urls import path

from .views import TrainingsViewSet, TrainingCategoryViewSet, \
    TrainingsFavoriteViewSet, TrainingsLikeViewSet, TrainingsCommentViewSet, TrainingRequestViewSet

app_name = 'trainings'

urlpatterns = [
    path('category/list/', TrainingCategoryViewSet.as_view({'get': "list_category"}),
         name='list_category'),

    path('create/', TrainingsViewSet.as_view({'post': "create_training"}),
         name='create_training'),
    path('update/<int:pk>/', TrainingsViewSet.as_view({'post': "partial_update_training"}),
         name='partial_update_training'),
    path('<int:pk>/', TrainingsViewSet.as_view({'get': "retrieve_training"}),
         name='retrieve_training'),
    path('list/<int:pk>/', TrainingsViewSet.as_view({'get': "list_training"}),
         name='list_training'),
    path('list/', TrainingsViewSet.as_view({'get': "list_all_training"}),
         name='list_all_training'),
    path('list_map/', TrainingsViewSet.as_view({'get': "list_all_training_for_map"}),
         name='list_all_training_for_map'),
    path('delete/', TrainingsViewSet.as_view({'post': "delete_training"}),
         name='delete_training'),

    path('like/create/', TrainingsLikeViewSet.as_view({'post': "create_like"}),
         name='training_create_like'),
    path('like/delete/<int:pk>/', TrainingsLikeViewSet.as_view({'delete': "delete_like"}),
         name='training_delete_like'),
    path('favorite/list/<int:pk>/', TrainingsFavoriteViewSet.as_view({'get': "list_favorite"}),
         name='training_list_favorite'),
    path('favorite/create/', TrainingsFavoriteViewSet.as_view({'post': "create_favorite"}),
         name='training_create_favorite'),
    path('favorite/delete/', TrainingsFavoriteViewSet.as_view({'post': "delete_favorite"}),
         name='training_delete_favorite'),
    path('comment/list/<int:pk>/', TrainingsCommentViewSet.as_view({'get': "list_comments"}),
         name='training_list_comments'),
     path('comment/delete/', TrainingsCommentViewSet.as_view({'post': "delete_comment"}),
         name='delete_comment'),
     path('comment/edit/', TrainingsCommentViewSet.as_view({'post': "edit_comment"}),
         name='edit_comment'),
    path('comment/create/', TrainingsCommentViewSet.as_view({'post': "create_comment"}),
         name='training_create_comment'),
    path('requests/create/', TrainingRequestViewSet.as_view({'post': "send_training_request"}),
         name='send_training_request'),
    path('requests/list_incoming/<int:pk>/', TrainingRequestViewSet.as_view({'get': "list_incoming_requests"}),
         name='list_incoming_requests'),
    path('requests/list_outgoing/<int:pk>/', TrainingRequestViewSet.as_view({'get': "list_outgoing_requests"}),
         name='list_outgoing_requests'),
    path('requests/change_request_status/', TrainingRequestViewSet.as_view({'post': "change_request_status"}),
         name='change_request_status'),


]
