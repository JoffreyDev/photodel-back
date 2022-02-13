from rest_framework import serializers
from gallery.models import Album, Gallery, Image, GalleryComment, GalleryLike, GalleryFavorite, \
    AlbumComment, AlbumLike, AlbumFavorite, PhotoSessionComment, PhotoSessionLike, \
    PhotoSessionFavorite, PhotoSession
from services.film_places_service import ImageBase64Field, Base64ImageField
from accounts.api.serializers import ProfilePublicSerializer, SpecializationListSerializer, \
    ProfileForGallerySerializer


# сериализаторы фото
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['id', 'photo', 'profile', ]


# сериализаторы альбома
class AlbumListSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    profile = ProfilePublicSerializer()
    main_photo_id = ImageSerializer()

    class Meta:
        model = Album
        fields = ['name_album', 'id', 'main_photo_id', 'profile', 'likes', 'comments', 'favorites', ]

    def get_likes(self, obj):
        return AlbumLike.objects.filter(album=obj.id).count()

    def get_comments(self, obj):
        return AlbumComment.objects.filter(album=obj.id).count()

    def get_favorites(self, obj):
        return AlbumFavorite.objects.filter(album=obj.id).count()


class AlbumForGallerySerializer(serializers.ModelSerializer):
    main_photo_id = ImageSerializer()
    count_photos = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['name_album', 'main_photo_id', 'count_photos', 'id', ]

    def get_count_photos(self, data):
        return data.gallery_set.all().count()


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def validate(self, data):
        profile = self.context['profile']
        user_albums = Album.objects.filter(profile=profile, name_album=data.get('name_album'))
        if user_albums:
            raise serializers.ValidationError({'error': 'Альбом с таким названием уже существует'})
        if not data.get('main_photo_id'):
            data['main_photo_id'] = Image.objects.filter(profile__user__username='admin').first()
        return data


class AlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def validate(self, data):
        profile = self.context['profile']
        user_albums = Album.objects.filter(profile=profile, name_album=data.get('name_album'))
        if user_albums:
            raise serializers.ValidationError({'error': 'Альбом с таким названием уже существует'})
        return data


class AlbumFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumFavorite
        fields = '__all__'


class AlbumFavoriteListSerializer(serializers.ModelSerializer):
    profile = ProfilePublicSerializer()
    album = AlbumListSerializer()

    class Meta:
        model = AlbumFavorite
        fields = ['profile', 'album', ]


class AlbumLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumLike
        fields = '__all__'


class AlbumCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumComment
        fields = '__all__'


class AlbumCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfileForGallerySerializer()
    album = AlbumListSerializer()

    class Meta:
        model = AlbumComment
        fields = ['content', 'timestamp', 'sender_comment', 'album', 'answer_id_comment', ]


# сериализаторы фото в галерее
class GalleryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['gallery_image', 'name_image', 'description', 'place_location', 'iso',
                  'string_place_location', 'photo_camera', 'focal_len', 'excerpt', 'flash',
                  'category', 'tags', 'album', 'profile', 'aperture', 'is_sell', 'is_hidden', ]

    def validate(self, data):
        """
        Если при создании фото не передан альбом, то фото добавляется в альбом Разное.
        Если при создании переданы альбомы, то проверяется,
        если в альбоме стоит дефолтная фотка, то на обложку альбома ставится фотка которая создается
        """
        if not data.get('album'):
            data['album'] = [Album.objects.filter(profile=self.context['profile']).first(), ]
        else:
            for album_id in data.get('album'):
                album = Album.objects.filter(id=album_id.id).first()
                if album.main_photo_id == Image.objects.filter(profile__user__username='admin').first():
                    album.main_photo_id = data.get('gallery_image')
                    album.save()
        return data


class GalleryForCardListSerializer(serializers.ModelSerializer):
    gallery_image = ImageSerializer()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['gallery_image', 'id', 'views', 'likes', 'comments',
                  'favorites', 'name_image', 'string_place_location', ]

    def get_likes(self, obj):
        return GalleryLike.objects.filter(gallery=obj.id).count()

    def get_comments(self, obj):
        return GalleryComment.objects.filter(gallery=obj.id).count()

    def get_favorites(self, obj):
        return GalleryFavorite.objects.filter(gallery=obj.id).count()


class GalleryListSerializer(serializers.ModelSerializer):
    gallery_image = ImageSerializer()
    album = AlbumForGallerySerializer(read_only=True, many=True)
    category = SpecializationListSerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    profile = ProfileForGallerySerializer()

    class Meta:
        model = Gallery
        fields = ['id', 'gallery_image', 'name_image', 'description', 'place_location', 'is_sell',
                  'photo_camera', 'focal_len', 'excerpt', 'flash', 'views', 'string_place_location',
                  'tags', 'category', 'album', 'profile', 'was_added', 'likes', 'is_hidden',
                  'comments', 'favorites', 'aperture', 'iso', ]

    def get_likes(self, obj):
        return GalleryLike.objects.filter(gallery=obj.id).count()

    def get_comments(self, obj):
        return GalleryComment.objects.filter(gallery=obj.id).count()

    def get_favorites(self, obj):
        return GalleryFavorite.objects.filter(gallery=obj.id).count()


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
    sender_comment = ProfileForGallerySerializer()
    gallery = GalleryForCardListSerializer()

    class Meta:
        model = GalleryComment
        fields = ['content', 'timestamp', 'sender_comment', 'gallery', 'answer_id_comment', ]


# сериализаторы фотоессий
class PhotoSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSession
        fields = '__all__'

    def validate(self, data):
        profile = self.context['profile']
        user_photo_session = PhotoSession.objects.filter(profile=profile, session_name=data.get('session_name'))
        if user_photo_session:
            raise serializers.ValidationError({'error': 'Фотосессия с таким названием уже существует'})
        return data


class PhotoSessionForCardListSerializer(serializers.ModelSerializer):
    main_photo = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['id', 'views', 'likes', 'comments', 'favorites', 'main_photo', ]

    def get_likes(self, obj):
        return PhotoSessionLike.objects.filter(photo_session=obj.id).count()

    def get_comments(self, obj):
        return PhotoSessionComment.objects.filter(photo_session=obj.id).count()

    def get_favorites(self, obj):
        return PhotoSessionFavorite.objects.filter(photo_session=obj.id).count()

    def get_main_photo(self, data):
        return '' if not data.photos.all() else data.photos.first().photo.url


class PhotoSessionListSerializer(serializers.ModelSerializer):
    session_сategory = SpecializationListSerializer()
    photos = ImageSerializer(read_only=True, many=True)
    profile = ProfileForGallerySerializer()

    class Meta:
        model = PhotoSession
        fields = ['id', 'session_name', 'session_description', 'session_location',
                  'string_session_location', 'session_date', 'session_сategory',
                  'photos', 'views', 'is_hidden', 'profile', ]


class PhotoSessionFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSessionFavorite
        fields = '__all__'


class PhotoSessionFavoriteListSerializer(serializers.ModelSerializer):
    profile = ProfilePublicSerializer()
    photo_session = PhotoSessionListSerializer()

    class Meta:
        model = PhotoSessionFavorite
        fields = ['profile', 'photo_session', ]


class PhotoSessionLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSessionLike
        fields = '__all__'


class PhotoSessionCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSessionComment
        fields = '__all__'


class PhotoSessionCommentListSerializer(serializers.ModelSerializer):
    sender_comment = ProfileForGallerySerializer()
    photo_session = PhotoSessionListSerializer()

    class Meta:
        model = PhotoSessionComment
        fields = ['content', 'timestamp', 'sender_comment', 'photo_session', 'answer_id_comment', ]
