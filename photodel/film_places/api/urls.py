from django.urls import path

from .views import FilmPlacesViewSet, CategoryFilmPlacesViewSet, \
    FilmPlacesFavoriteViewSet, FilmPlacesLikeViewSet, FilmPlacesCommentViewSet, \
    FilmRequestViewSet

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
    path('best/list/', FilmPlacesViewSet.as_view({'get': "the_best_places"}),
         name='the_best_places'),
    path('delete/', FilmPlacesViewSet.as_view({'post': "delete_place"}),
         name='delete_place'),

    path('like/create/', FilmPlacesLikeViewSet.as_view({'post': "create_like"}),
         name='place_create_like'),
    path('like/delete/<int:pk>/', FilmPlacesLikeViewSet.as_view({'delete': "delete_like"}),
         name='place_delete_like'),
    path('favorite/list/', FilmPlacesFavoriteViewSet.as_view({'get': "list_favorite"}),
         name='place_list_favorite'),
    path('favorite/create/', FilmPlacesFavoriteViewSet.as_view({'post': "create_favorite"}),
         name='place_create_favorite'),
    path('favorite/delete/<int:pk>/', FilmPlacesFavoriteViewSet.as_view({'delete': "delete_favorite"}),
         name='place_delete_favorite'),
    path('comment/list/<int:pk>/', FilmPlacesCommentViewSet.as_view({'get': "list_comments"}),
         name='place_list_comments'),
    path('comment/create/', FilmPlacesCommentViewSet.as_view({'post': "create_comment"}),
         name='place_create_comment'),

    path('film_request/create/', FilmRequestViewSet.as_view({'post': "create_film_request"}),
         name='create_film_request'),
]

