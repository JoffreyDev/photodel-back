from django.urls import path

from .views import FilmPlacesViewSet, CategoryFilmPlacesViewSet, \
    FilmPlacesFavoriteViewSet, FilmPlacesLikeViewSet, FilmPlacesCommentViewSet

app_name = 'film_places'

urlpatterns = [
    path('create/', FilmPlacesViewSet.as_view({'post': "create_place"}),
         name='create_place'),
    path('list/', CategoryFilmPlacesViewSet.as_view({'get': "list_category"}),
         name='list_category'),
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
]

