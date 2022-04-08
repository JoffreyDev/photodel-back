from gallery.models import GalleryFavorite, GalleryLike, Gallery, GalleryComment, \
    PhotoSessionLike, PhotoSessionFavorite, PhotoSessionComment, PhotoSession
from film_places.models import FilmPlacesLike, FilmPlacesFavorite, FilmPlacesComment, \
    FilmPlaces, FilmRequest
from accounts.models import ProfileLike, ProfileFavorite, ProfileComment
from django.db.models import Sum


def get_count_profile_comments(profile):
    me_profile_comments = ProfileComment.objects.filter(receiver_comment=profile).count()
    me_photo_comments = GalleryComment.objects.filter(gallery__profile=profile).count()
    me_session_comments = PhotoSessionComment.objects.filter(photo_session__profile=profile).count()
    me_place_comments = FilmPlacesComment.objects.filter(place__profile=profile).count()

    my_profile_comments = ProfileComment.objects.filter(sender_comment=profile).count()
    my_photo_comments = GalleryComment.objects.filter(sender_comment=profile).count()
    my_session_comments = PhotoSessionComment.objects.filter(sender_comment=profile).count()
    my_place_comments = FilmPlacesComment.objects.filter(sender_comment=profile).count()

    return {
        "me_count_commetns": me_photo_comments + me_session_comments + me_profile_comments + me_place_comments,
        "my_count_commetns": my_photo_comments + my_session_comments + my_profile_comments + my_place_comments
    }


def get_count_profile_favorite(profile):
    me_profile_favorites = ProfileFavorite.objects.filter(sender_favorite=profile).count()
    me_photo_favorites = GalleryFavorite.objects.filter(gallery__profile=profile).count()
    me_session_favorites = PhotoSessionFavorite.objects.filter(photo_session__profile=profile).count()
    me_place_favorites = FilmPlacesFavorite.objects.filter(place__profile=profile).count()

    my_profile_favorites = ProfileFavorite.objects.filter(receiver_favorite=profile).count()
    my_photo_favorites = GalleryFavorite.objects.filter(profile=profile).count()
    my_session_favorites = PhotoSessionFavorite.objects.filter(profile=profile).count()
    my_place_favorites = FilmPlacesFavorite.objects.filter(profile=profile).count()

    return {
        "me_count_favorites": me_profile_favorites + me_photo_favorites + me_session_favorites + me_place_favorites,
        "my_count_favorites": my_profile_favorites + my_photo_favorites + my_session_favorites + my_place_favorites
    }


def get_count_profile_like(profile):
    me_profile_likes = ProfileLike.objects.filter(receiver_like=profile).count()
    me_photo_likes = GalleryLike.objects.filter(gallery__profile=profile).count()
    me_session_likes = PhotoSessionLike.objects.filter(photo_session__profile=profile).count()
    me_place_likes = FilmPlacesLike.objects.filter(place__profile=profile).count()

    my_profile_likes = ProfileLike.objects.filter(sender_like=profile).count()
    my_photo_likes = GalleryLike.objects.filter(profile=profile).count()
    my_session_likes = PhotoSessionLike.objects.filter(profile=profile).count()
    my_place_likes = FilmPlacesLike.objects.filter(profile=profile).count()

    return {
        "me_count_likes": me_profile_likes + me_photo_likes + me_session_likes + me_place_likes,
        "my_count_likes": my_profile_likes + my_photo_likes + my_session_likes + my_place_likes
    }


def get_count_profile_views(profile):
    me_profile_views = profile.views
    me_photo_views = int(Gallery.objects.filter(profile=profile).aggregate(Sum('views')).get('views__sum') or 0)
    me_session_views = int(PhotoSession.objects.filter(profile=profile).aggregate(Sum('views')).get('views__sum') or 0)
    me_place_views = int(FilmPlaces.objects.filter(profile=profile).aggregate(Sum('views')).get('views__sum') or 0)

    return {
        "me_count_views": me_profile_views + me_photo_views + me_session_views + me_place_views,
    }


def get_count_profile_request(profile):
    me_request = FilmRequest.objects.filter(receiver_profile=profile).count()
    my_request = FilmRequest.objects.filter(profile=profile).count()

    return {
        "me_requests": me_request,
        "my_requests": my_request
    }


def collect_profile_statistics(profile):
    common = {}
    comments = get_count_profile_comments(profile)
    favorites = get_count_profile_favorite(profile)
    likes = get_count_profile_like(profile)
    views = get_count_profile_views(profile)
    requests = get_count_profile_request(profile)
    common.update(comments)
    common.update(favorites)
    common.update(likes)
    common.update(views)
    common.update(requests)
    return common
