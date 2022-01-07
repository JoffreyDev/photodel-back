from django.db import models
from django.utils import timezone
from accounts.models import Profile, Specialization
from django.contrib.gis.db import models as gis_models
from django.core.validators import MaxValueValidator, MinValueValidator


class Image(models.Model):
    photo = models.ImageField(upload_to='gallery/')


class Album(models.Model):
    name_album = models.CharField(max_length=40)
    description_album = models.TextField(blank=True)
    main_photo_id = models.IntegerField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Gallery(models.Model):
    gallery_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    name_image = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    place_location = gis_models.PointField(srid=4326)
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


class PhotoSession(models.Model):
    session_name = models.CharField(max_length=40)
    session_description = models.TextField(blank=True)
    session_location = gis_models.PointField(srid=4326)
    session_date = models.DateField()
    session_type = models.CharField(max_length=50)
    photos = models.ManyToManyField(Image)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class GalleryComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    sender_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class GalleryLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class GalleryFavorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
