from django.urls import path
from .views import AlbumViewSet, GalleryViewSet, GalleryFavoriteViewSet, \
    GalleryLikeViewSet, GalleryCommentViewSet, ImageViewSet, PhotoSessionViewSet, \
    PhotoSessionFavoriteViewSet, PhotoSessionLikeViewSet, PhotoSessionCommentViewSet, ReviewViewSet

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
    path('album/<int:pk>/', AlbumViewSet.as_view({'get': "retrieve_album"}),
         name='retrieve_album'),
    path('album/list_photos_without_album/<int:pk>/', AlbumViewSet.as_view({'get': "list_photos_not_in_album"}),
         name='list_photos_not_in_album'),
    path('album/add_photos/', AlbumViewSet.as_view({'post': "add_to_album_photos"}),
         name='list_user_albums'),
    path('album/delete_photos/', AlbumViewSet.as_view({'post': "delete_from_album_photos"}),
         name='list_user_albums'),
    path('album/delete/', AlbumViewSet.as_view({'post': "delete_album"}),
         name='delete_album'),

    # урлы фото в галлерее
    path('photo/create/', GalleryViewSet.as_view({'post': "create_photo"}),
         name='create_photo'),
    path('photo/update/<int:pk>/', GalleryViewSet.as_view({'post': "partial_update_photo"}),
         name='partial_update_photo'),
    path('photo/<int:pk>/', GalleryViewSet.as_view({'get': "retrieve_photo"}),
         name='retrieve_photo'),
    path('photo/list/<int:pk>/', GalleryViewSet.as_view({'get': "list_photos"}),
         name='list_photos'),
    path('photo/list/', GalleryViewSet.as_view({'get': "list_all_photos"}),
         name='list_all_photos'),
    path('photo/list_map/', GalleryViewSet.as_view({'get': "list_all_photos_for_map"}),
         name='list_all_photos_for_map'),
    path('photo/popular/', GalleryViewSet.as_view({'get': "popular_photos"}),
         name='popular_photos'),
    path('photo/delete/', GalleryViewSet.as_view({'post': "delete_photo"}),
         name='delete_photo'),
    path('photo/favorite/list/<int:pk>/', GalleryFavoriteViewSet.as_view({'get': "list_favorite"}),
         name='list_favorite'),
    path('photo/favorite/create/', GalleryFavoriteViewSet.as_view({'post': "create_favorite"}),
         name='create_favorite'),
    path('photo/favorite/delete/', GalleryFavoriteViewSet.as_view({'post': "delete_favorite"}),
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
    path('photo_session/delete/', PhotoSessionViewSet.as_view({'post': "delete_photo_session"}),
         name='delete_photo_session'),
    path('photo_session/favorite/list/<int:pk>/', PhotoSessionFavoriteViewSet.as_view({'get': "list_favorite"}),
         name='list_favorite'),
    path('photo_session/favorite/create/', PhotoSessionFavoriteViewSet.as_view({'post': "create_favorite"}),
         name='create_favorite'),
    path('photo_session/favorite/delete/', PhotoSessionFavoriteViewSet.as_view({'post': "delete_favorite"}),
         name='delete_favorite'),
    path('photo_session/like/create/', PhotoSessionLikeViewSet.as_view({'post': "create_like"}),
         name='create_like'),
    path('photo_session/like/delete/<int:pk>/', PhotoSessionLikeViewSet.as_view({'delete': "delete_like"}),
         name='delete_like'),
    path('photo_session/comment/list/<int:pk>/', PhotoSessionCommentViewSet.as_view({'get': "list_comments"}),
         name='list_comments'),
    path('photo_session/comment/create/', PhotoSessionCommentViewSet.as_view({'post': "create_comment"}),
         name='create_comment'),

    # отзывы
    path('review/create/', ReviewViewSet.as_view({'post': "create_review"}),
         name='create_review'),
    path('review/update/<int:pk>/', ReviewViewSet.as_view({'post': "update_review"}),
         name='update_review'),
    path('review/list/<int:pk>/', ReviewViewSet.as_view({'get': "list_reviews"}),
         name='list_reviews'),

]
