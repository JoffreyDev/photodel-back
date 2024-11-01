from django.urls import path

from .views import FilmPlacesViewSet, CategoryFilmPlacesViewSet, \
    FilmPlacesFavoriteViewSet, FilmPlacesLikeViewSet, FilmPlacesCommentViewSet, \
    FilmRequestViewSet, NotAuthFilmRequestViewSet

app_name = 'film_places'

urlpatterns = [
    path('category/list/', CategoryFilmPlacesViewSet.as_view({'get': "list_category"}),
         name='list_category'),

    path('create/', FilmPlacesViewSet.as_view({'post': "create_place"}),
         name='create_place'),
    path('update/<int:pk>/', FilmPlacesViewSet.as_view({'post': "partial_update_place"}),
         name='partial_update_place'),
    path('<int:pk>/', FilmPlacesViewSet.as_view({'get': "retrieve_place"}),
         name='retrieve_place'),
    path('list/<int:pk>/', FilmPlacesViewSet.as_view({'get': "list_place"}),
         name='list_place'),
    path('list/', FilmPlacesViewSet.as_view({'get': "list_all_place"}),
         name='list_all_place'),
    path('list_map/', FilmPlacesViewSet.as_view({'get': "list_all_place_for_map"}),
         name='list_all_place_for_map'),
    path('best/list/', FilmPlacesViewSet.as_view({'get': "the_best_places"}),
         name='the_best_places'),
    path('delete/', FilmPlacesViewSet.as_view({'post': "delete_place"}),
         name='delete_place'),

    path('like/create/', FilmPlacesLikeViewSet.as_view({'post': "create_like"}),
         name='place_create_like'),
    path('like/delete/<int:pk>/', FilmPlacesLikeViewSet.as_view({'delete': "delete_like"}),
         name='place_delete_like'),
    path('favorite/list/<int:pk>/', FilmPlacesFavoriteViewSet.as_view({'get': "list_favorite"}),
         name='place_list_favorite'),
    path('favorite/create/', FilmPlacesFavoriteViewSet.as_view({'post': "create_favorite"}),
         name='place_create_favorite'),
    path('favorite/delete/', FilmPlacesFavoriteViewSet.as_view({'post': "delete_favorite"}),
         name='place_delete_favorite'),
    path('comment/list/<int:pk>/', FilmPlacesCommentViewSet.as_view({'get': "list_comments"}),
         name='place_list_comments'),
      path('comment/edit/', FilmPlacesCommentViewSet.as_view({'post': "edit_comment"}),
         name='edit_comment'),
     path('comment/delete/', FilmPlacesCommentViewSet.as_view({'post': "delete_comment"}),
         name='delete_comment'),
    path('comment/create/', FilmPlacesCommentViewSet.as_view({'post': "create_comment"}),
         name='place_create_comment'),

    path('film_request/create/', FilmRequestViewSet.as_view({'post': "create_film_request"}),
         name='create_film_request'),
    path('film_request/list_incoming/<int:pk>/', FilmRequestViewSet.as_view({'get': "list_incoming_request"}),
         name='list_incoming_request'),
    path('film_request/list_outgoing/<int:pk>/', FilmRequestViewSet.as_view({'get': "list_outgoing_request"}),
         name='list_outgoing_request'),
    path('add_reason_failure/<int:pk>/', FilmRequestViewSet.as_view({'post': "add_reason_failure"}),
         name='add_reason_failure'),

    path('create_not_auth_film_request/', NotAuthFilmRequestViewSet.as_view({'post': "create_not_auth_film_request"}),
         name='create_not_auth_film_request'),
    path('confirm_email/', NotAuthFilmRequestViewSet.as_view({'post': "confirm_email"}),
         name='confirm_email'),
    path('list_not_auth_requests/', NotAuthFilmRequestViewSet.as_view({'get': "list_not_auth_requests"}),
         name='list_not_auth_requests'),
    path('retrieve_not_auth_requests/<int:pk>/', NotAuthFilmRequestViewSet.as_view({'get': "retrieve_not_auth_requests"}),
         name='retrieve_not_auth_requests'),

]

