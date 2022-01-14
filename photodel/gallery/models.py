from django.db import models
from django.utils import timezone
from accounts.models import Profile, Specialization
from django.contrib.gis.db import models as gis_models
from django.core.validators import MaxValueValidator, MinValueValidator


def image_path(instance, filename):
    return f'gallery/{instance.profile.id}.jpg'


class Image(models.Model):
    photo = models.ImageField(upload_to=image_path)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class Album(models.Model):
    name_album = models.CharField(max_length=40)
    description_album = models.TextField(blank=True)
    main_photo_id = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_album


class AlbumComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    sender_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class AlbumLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class AlbumFavorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Gallery(models.Model):
    gallery_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    name_image = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    place_location = gis_models.PointField(srid=4326)
    string_place_location = gis_models.PointField(srid=4326, null=True)
    tags = models.TextField(blank=True, null=True)
    photo_camera = models.CharField(max_length=40)
    focal_len = models.CharField(max_length=40)
    excerpt = models.CharField(max_length=40)
    flash = models.CharField(max_length=40)
    last_ip_user = models.CharField(max_length=18, null=True, blank=True)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True)
    album = models.ManyToManyField(Album, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_image


class GalleryComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    sender_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class GalleryLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class GalleryFavorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class PhotoSession(models.Model):
    session_name = models.CharField(max_length=40)
    session_description = models.TextField(blank=True)
    session_location = gis_models.PointField(srid=4326)
    session_date = models.DateField()
    session_type = models.CharField(max_length=50)
    photos = models.ManyToManyField(Image)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_name


class PhotoSessionComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    sender_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo_session = models.ForeignKey(PhotoSession, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class PhotoSessionLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo_session = models.ForeignKey(PhotoSession, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class PhotoSessionFavorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo_session = models.ForeignKey(PhotoSession, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
