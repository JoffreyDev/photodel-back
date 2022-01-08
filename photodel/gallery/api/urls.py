from django.urls import path
from .views import AlbumViewSet, GalleryViewSet, GalleryFavoriteViewSet, \
     GalleryLikeViewSet, GalleryCommentViewSet, ImageViewSet

app_name = 'gallery'

urlpatterns = [
     path('image/create/', ImageViewSet.as_view({'post': "create_image"}),
          name='create_image'),

     path('album/create/', AlbumViewSet.as_view({'post': "create_album"}),
          name='create_album'),
     path('album/list/<int:pk>/', AlbumViewSet.as_view({'get': "list_user_albums"}),
          name='list_user_albums'),
     path('album/list_photos/<int:pk>/', AlbumViewSet.as_view({'get': "list_album_photos"}),
          name='list_album_photos'),
     path('album/delete/<int:album_id>/<int:photo_id>/', AlbumViewSet.as_view({'get': "delete_photo_from_album"}),
          name='delete_photo_from_album'),

     path('photo/create/', GalleryViewSet.as_view({'post': "create_photo"}),
          name='create_photo'),
     path('photo/<int:pk>/', GalleryViewSet.as_view({'get': "retrieve_photo"}),
          name='retrieve_photo'),
     path('photo/list/<int:pk>/', GalleryViewSet.as_view({'get': "list_photos"}),
          name='list_photos'),
     path('photo/like/create/', GalleryLikeViewSet.as_view({'post': "create_like"}),
          name='create_like'),
     path('photo/like/delete/<int:pk>/', GalleryLikeViewSet.as_view({'delete': "delete_like"}),
          name='delete_like'),
     path('photo/favorite/list/', GalleryFavoriteViewSet.as_view({'get': "list_favorite"}),
          name='list_favorite'),
     path('photo/favorite/create/', GalleryFavoriteViewSet.as_view({'post': "create_favorite"}),
          name='create_favorite'),
     path('photo/favorite/delete/<int:pk>/', GalleryFavoriteViewSet.as_view({'delete': "delete_favorite"}),
          name='delete_favorite'),
     path('photo/comment/list/<int:pk>/', GalleryCommentViewSet.as_view({'get': "list_comments"}),
          name='list_comments'),
     path('photo/comment/create/', GalleryCommentViewSet.as_view({'post': "create_comment"}),
          name='create_comment'),

]
