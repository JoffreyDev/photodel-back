from django.urls import path
from .views import AlbumViewSet, GalleryViewSet, GalleryFavoriteViewSet, \
     GalleryLikeViewSet, GalleryCommentViewSet, ImageViewSet, AlbumLikeViewSet, \
     AlbumFavoriteViewSet, AlbumCommentViewSet, PhotoSessionViewSet, \
     PhotoSessionFavoriteViewSet, PhotoSessionLikeViewSet, PhotoSessionCommentViewSet

app_name = 'gallery'

urlpatterns = [
     # урлы фото
     path('image/create/', ImageViewSet.as_view({'post': "create_image"}),
          name='create_image'),

     # урлы альбома
     path('album/create/', AlbumViewSet.as_view({'post': "create_album"}),
          name='create_album'),
     path('album/update/<int:pk>/', AlbumViewSet.as_view({'post': "partial_update"}),
          name='partial_update'),
     path('album/list/<int:pk>/', AlbumViewSet.as_view({'get': "list_user_albums"}),
          name='list_user_albums'),
     path('album/list_photos/<int:pk>/', AlbumViewSet.as_view({'get': "list_album_photos"}),
          name='list_album_photos'),
     path('album/list_photos_without_album/<int:pk>/', AlbumViewSet.as_view({'get': "list_photos_not_in_album"}),
          name='list_photos_not_in_album'),
     path('album/add_photos/', AlbumViewSet.as_view({'post': "add_to_album_photos"}),
          name='list_user_albums'),
     path('album/delete_photos/', AlbumViewSet.as_view({'post': "delete_from_album_photos"}),
          name='list_user_albums'),
     path('album/delete/<int:pk>/', AlbumViewSet.as_view({'delete': "delete_album"}),
          name='delete_album'),
     path('album/favorite/list/', AlbumFavoriteViewSet.as_view({'get': "list_favorite"}),
          name='album_list_favorite'),
     path('album/favorite/create/', AlbumFavoriteViewSet.as_view({'post': "create_favorite"}),
          name='album_create_favorite'),
     path('album/favorite/delete/<int:pk>/', AlbumFavoriteViewSet.as_view({'delete': "delete_favorite"}),
          name='album_delete_favorite'),
     path('album/like/create/', AlbumLikeViewSet.as_view({'post': "create_like"}),
          name='album_create_like'),
     path('album/like/delete/<int:pk>/', AlbumLikeViewSet.as_view({'delete': "delete_like"}),
          name='album_delete_like'),
     path('album/comment/list/<int:pk>/', AlbumCommentViewSet.as_view({'get': "list_comments"}),
          name='album_list_comments'),
     path('album/comment/create/', AlbumCommentViewSet.as_view({'post': "create_comment"}),
          name='album_create_comment'),

     # урлы фото в галлерее
     path('photo/create/', GalleryViewSet.as_view({'post': "create_photo"}),
          name='create_photo'),
     path('photo/update/<int:pk>/', GalleryViewSet.as_view({'post': "partial_update_photo"}),
          name='partial_update_photo'),
     path('photo/<int:pk>/', GalleryViewSet.as_view({'get': "retrieve_photo"}),
          name='retrieve_photo'),
     path('photo/list/<int:pk>/', GalleryViewSet.as_view({'get': "list_photos"}),
          name='list_photos'),
     path('photo/delete/<int:pk>/', GalleryViewSet.as_view({'delete': "delete_photo"}),
          name='delete_photo'),
     path('photo/favorite/list/', GalleryFavoriteViewSet.as_view({'get': "list_favorite"}),
          name='list_favorite'),
     path('photo/favorite/create/', GalleryFavoriteViewSet.as_view({'post': "create_favorite"}),
          name='create_favorite'),
     path('photo/favorite/delete/<int:pk>/', GalleryFavoriteViewSet.as_view({'delete': "delete_favorite"}),
          name='delete_favorite'),
     path('photo/like/create/', GalleryLikeViewSet.as_view({'post': "create_like"}),
          name='create_like'),
     path('photo/like/delete/<int:pk>/', GalleryLikeViewSet.as_view({'delete': "delete_like"}),
          name='delete_like'),
     path('photo/comment/list/<int:pk>/', GalleryCommentViewSet.as_view({'get': "list_comments"}),
          name='list_comments'),
     path('photo/comment/create/', GalleryCommentViewSet.as_view({'post': "create_comment"}),
          name='create_comment'),

     # урлы фотосессии
     path('photo_session/create/', PhotoSessionViewSet.as_view({'post': "create_photo_session"}),
          name='create_photo_session'),
     path('photo_session/update/<int:pk>/', PhotoSessionViewSet.as_view({'post': "partial_update_photo_session"}),
          name='partial_update_photo_session'),
     path('photo_session/<int:pk>/', PhotoSessionViewSet.as_view({'get': "retrieve_photo_session"}),
          name='retrieve_photo_session'),
     path('photo_session/list/<int:pk>/', PhotoSessionViewSet.as_view({'get': "list_photo_sessions"}),
          name='list_photo_sessions'),
     path('photo_session/delete/<int:pk>/', PhotoSessionViewSet.as_view({'delete': "delete_photo_session"}),
          name='delete_photo_session'),

     path('photo_session/favorite/list/', PhotoSessionFavoriteViewSet.as_view({'get': "list_favorite"}),
          name='list_favorite'),
     path('photo_session/favorite/create/', PhotoSessionFavoriteViewSet.as_view({'post': "create_favorite"}),
          name='create_favorite'),
     path('photo_session/favorite/delete/<int:pk>/', PhotoSessionFavoriteViewSet.as_view({'delete': "delete_favorite"}),
          name='delete_favorite'),
     path('photo_session/like/create/', PhotoSessionLikeViewSet.as_view({'post': "create_like"}),
          name='create_like'),
     path('photo_session/like/delete/<int:pk>/', PhotoSessionLikeViewSet.as_view({'delete': "delete_like"}),
          name='delete_like'),
     path('photo_session/comment/list/<int:pk>/', PhotoSessionCommentViewSet.as_view({'get': "list_comments"}),
          name='list_comments'),
     path('photo_session/comment/create/', PhotoSessionCommentViewSet.as_view({'post': "create_comment"}),
          name='create_comment'),

]
