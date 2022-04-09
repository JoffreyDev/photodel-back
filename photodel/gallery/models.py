from django.db import models
from django.utils import timezone
from accounts.models import Profile, Specialization
from django.contrib.gis.db import models as gis_models
from django.core.validators import MaxValueValidator, MinValueValidator


def image_path(instance, filename):
    return f'gallery/{instance.profile.id}.jpg'


def get_photo():
    image = Image.objects.filter(profile__user__username='admin').first()
    return image


class Image(models.Model):
    photo = models.ImageField(upload_to=image_path)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class Album(models.Model):
    name_album = models.CharField(max_length=40)
    description_album = models.TextField(blank=True)
    main_photo_id = models.ForeignKey(Image, on_delete=models.SET(get_photo), blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name_album


class Gallery(models.Model):
    gallery_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    name_image = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    place_location = gis_models.PointField(srid=4326)
    string_place_location = models.CharField(max_length=40, null=True, blank=True)
    tags = models.TextField(blank=True, null=True)
    photo_camera = models.CharField(max_length=40, blank=True)
    focal_len = models.CharField(max_length=40, blank=True)
    excerpt = models.CharField(max_length=40, blank=True)
    aperture = models.CharField(max_length=40, null=True, blank=True)
    iso = models.CharField(max_length=40, null=True, blank=True)
    flash = models.CharField(max_length=40, blank=True)
    is_sell = models.BooleanField(default=False)
    last_ip_user = models.CharField(max_length=18, null=True, blank=True)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    was_added = models.DateTimeField(default=timezone.localtime)
    is_hidden = models.BooleanField(default=False)
    category = models.ManyToManyField(Specialization)
    album = models.ManyToManyField(Album, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_image


class GalleryComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    answer_id_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='gallery_comment_answer')
    quote_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='gallery_comment_quote')
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
    string_session_location = models.CharField(max_length=40, null=True, blank=True)
    session_date = models.DateField()
    session_category = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    photos = models.ManyToManyField(Image, related_name='rel_images')
    main_photo = models.ForeignKey(Image, on_delete=models.SET(get_photo), blank=True, null=True, related_name='main')
    last_ip_user = models.CharField(max_length=18, null=True, blank=True)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    is_hidden = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_name


class PhotoSessionComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    answer_id_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='photo_session_comment_answer')
    quote_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='photo_session_gallery_comment_quote')
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
