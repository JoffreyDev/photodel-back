from django.db import models
from django.contrib.gis.db import models as gis_models
from accounts.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from gallery.models import Image
from django.utils import timezone


def get_photo():
    image = Image.objects.filter(profile__user__username='admin').first()
    return image


class TrainingCategory(models.Model):
    name_category = models.CharField(max_length=40)

    def __str__(self):
        return self.name_category


class Trainings(models.Model):
    PLACE_CHOICES = [
        ('Online', 'Онлайн'),
        ('Offline', 'Оффлайн'),
    ]

    training_title = models.CharField(max_length=50)
    training_images = models.ManyToManyField(Image)
    training_description = models.TextField(blank=True)
    place = models.CharField(choices=PLACE_CHOICES,
                             max_length=20, default='Оффлайн')
    summary_members = models.IntegerField(default=10)
    reserved_places = models.IntegerField(default=0)
    place_location = gis_models.PointField(srid=4326)
    string_place_location = models.CharField(
        max_length=60, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    views = models.IntegerField(default=0, validators=[MinValueValidator(0.0)])
    main_photo = models.ForeignKey(Image, on_delete=models.SET(get_photo), blank=True, null=True,
                                   related_name='trainings_main_photo')
    is_hidden = models.BooleanField(default=False)
    was_added = models.DateTimeField(default=timezone.localtime)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes_stat = models.IntegerField(
        default=0, validators=[MinValueValidator(0.0)])
    training_team = models.ManyToManyField(
        Profile, blank=True,  related_name='trainings_team')
    training_orgs = models.ManyToManyField(
        Profile, blank=True,  related_name='training_orgs')
    training_members = models.ManyToManyField(
        Profile, blank=True,  related_name='trainings_members')
    training_category = models.ForeignKey(
        TrainingCategory, blank=True, null=True, related_name='trainings_category', on_delete=models.CASCADE)
    count_interested_in = models.IntegerField(
        default=0, validators=[MinValueValidator(0.0)])
    cost = models.IntegerField(
        default=0, validators=[MinValueValidator(0.0)])
    first_payment = models.IntegerField(
        default=0, validators=[MinValueValidator(0.0)])
    last_ip_user = models.CharField(max_length=18, null=True, blank=True)

    def __str__(self):
        return self.training_title


class TrainingsComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    answer_id_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='trainings_comment_answer')
    quote_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='trainings_comment_quote')
    sender_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    training = models.ForeignKey(Trainings, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class TrainingsLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    training = models.ForeignKey(Trainings, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class TrainingsFavorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    training = models.ForeignKey(Trainings, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class TrainingsRequest(models.Model):
    training = models.ForeignKey(
        Trainings, on_delete=models.CASCADE, related_name='training')
    request_user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='request_user')
    STATUS_CHOICES = [
        ('AWAITING', 'Ожидает'),
        ('ACCEPTED', 'Принят'),
        ('REJECTED', 'Отклонен'),
    ]
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='AWAITING')

    def __str__(self):
        return str(self.id)
