from django.db import models
from django.contrib.gis.db import models as gis_models
from accounts.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from gallery.models import Image
from django.utils import timezone


def get_photo():
    image = Image.objects.filter(profile__user__username='admin').first()
    return image


class CategoryFilmPlaces(models.Model):
    name_category = models.CharField(max_length=40)

    def __str__(self):
        return self.name_category


class FilmPlaces(models.Model):
    name_place = models.CharField(max_length=50)
    place_image = models.ManyToManyField(Image)
    description = models.TextField(blank=True)
    photo_camera = models.CharField(max_length=40)
    cost = models.CharField(max_length=10)
    payment = models.CharField(max_length=40)
    place_location = gis_models.PointField(srid=4326)
    string_place_location = models.CharField(max_length=40, null=True, blank=True)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0.0)])
    main_photo = models.ForeignKey(Image, on_delete=models.SET(get_photo), blank=True, null=True,
                                   related_name='film_places_main_photo')
    last_views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    last_ip_user = models.CharField(max_length=18, null=True, blank=True)
    is_hidden = models.BooleanField(default=False)
    category = models.ManyToManyField(CategoryFilmPlaces)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_place


class FilmPlacesComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    answer_id_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='film_places_comment_answer')
    quote_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='film_places_comment_quote')
    sender_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(FilmPlaces, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class FilmPlacesLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(FilmPlaces, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class FilmPlacesFavorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(FilmPlaces, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class FilmRequest(models.Model):
    FILMING_STATUS_CHOICES = [
        ('NEW', 'Новый'),
        ('ACCEPTED', 'Принят'),
        ('COMPLETED', 'Завершен'),
        ('UNCOMPLETED', 'Не завершен'),
        ('REJECTED', 'Отклонен'),
    ]

    filming_timestamp = models.DateTimeField()
    hours_duration = models.IntegerField()
    string_filming_location = models.CharField(max_length=40, blank=True)
    filming_type = models.CharField(max_length=40)
    filming_status = models.CharField(max_length=12, choices=FILMING_STATUS_CHOICES, default='NEW')
    count_person = models.IntegerField()
    filming_budget = models.FloatField()
    need_makeup_artist = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    was_added = models.DateTimeField(default=timezone.localtime)
    place = models.ForeignKey(FilmPlaces, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
