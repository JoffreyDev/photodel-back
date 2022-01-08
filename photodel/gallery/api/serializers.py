from rest_framework import serializers
from gallery.models import Album, Gallery, GalleryComment, GalleryLike, GalleryFavorite, Image, PhotoSession
from services.film_places_service import ImageBase64Field, Base64ImageField
from accounts.api.serializers import ProfilePublicSerializer


class ImageSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = ['id', 'photo', ]


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name_album', 'description_album', ]


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class GalleryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryForCardListSerializer(serializers.ModelSerializer):
    gallery_image = ImageSerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['gallery_image', 'id', 'views', 'likes', 'comments', 'favorites', ]

    def get_likes(self, obj):
        return GalleryLike.objects.filter(gallery=obj.id).count()

    def get_comments(self, obj):
        return GalleryComment.objects.filter(gallery=obj.id).count()

    def get_favorites(self, obj):
        return GalleryFavorite.objects.filter(gallery=obj.id).count()


class GalleryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['gallery_image', 'name_image', 'description', 'place_location',
                  'photo_camera', 'focal_len', 'excerpt', 'flash', 'views', ]


class PhotoSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSession
        fields = '__all__'


class GalleryFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryFavorite
        fields = '__all__'


class GalleryFavoriteListSerializer(serializers.ModelSerializer):
    profile = ProfilePublicSerializer()
    gallery = GalleryForCardListSerializer()

    class Meta:
        model = GalleryFavorite
        fields = ['profile', 'gallery', ]


class GalleryLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryLike
        fields = '__all__'


class GalleryCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryComment
        fields = '__all__'


class GalleryCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfilePublicSerializer()
    gallery = GalleryForCardListSerializer()

    class Meta:
        model = GalleryComment
        fields = ['content', 'timestamp', 'sender_comment', 'gallery', ]
