from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User
from additional_entities.models import Country, Language
from django.core.validators import MaxValueValidator, MinValueValidator


class Specialization(models.Model):
    name_spec = models.CharField(max_length=50)

    def __str__(self):
        return self.name_spec


class ProCategory(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name_category


class Profile(models.Model):
    READY_STATUS_CHOICES = [
        ('BUSY', 'Занят'),
        ('FREE', 'Свободен'),
    ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    avatar = models.ImageField(
        upload_to='avatars/', default='default_images/anonymous.jpg')
    date_register = models.DateTimeField(default=timezone.localtime)
    last_date_in = models.DateTimeField(null=True, blank=True)
    last_ip = models.CharField(max_length=15, blank=True)
    filming_geo = models.ManyToManyField(Country, blank=True)
    work_condition = models.CharField(max_length=100, blank=True)
    cost_services = models.CharField(max_length=100, blank=True)
    photo_technics = models.CharField(max_length=50, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    about = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=1)  # 1 - Клиент 2 - Профи
    # 0 - Бесплатный, 1 - Стандарт, 2 - Максимум
    pay_status = models.IntegerField(default=0)
    ready_status = models.CharField(
        max_length=50, blank=True, choices=READY_STATUS_CHOICES)
    type_pro = models.ForeignKey(
        ProCategory, on_delete=models.CASCADE, null=True)
    spec_model_or_photographer = models.ManyToManyField(
        Specialization, blank=True)
    # 1 - Бесплатный 2 - Стандарт 3 - Максимум
    type_pro_account = models.IntegerField(default=1, null=True)
    expired_pro_subscription = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    # contacts
    location = gis_models.PointField(srid=4326, blank=True, null=True)
    string_location = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, blank=True)
    site = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=50)
    email_verify = models.BooleanField(default=False)
    instagram = models.CharField(max_length=40, blank=True)
    facebook = models.CharField(max_length=40, blank=True)
    vk = models.CharField(max_length=40, blank=True)

    # temporary geolocation
    location_now = gis_models.PointField(srid=4326, blank=True, null=True)
    string_location_now = models.CharField(
        max_length=50, null=True, blank=True)
    date_stay_start = models.DateTimeField(blank=True, null=True)
    date_stay_end = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True)

    is_adult = models.BooleanField(default=False)
    is_show_nu_photo = models.BooleanField(default=False)
    is_hide = models.BooleanField(default=False)
    is_change = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    last_views = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    user_channel_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


class ProfileComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    answer_id_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='profile_comment_answer')
    quote_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='profile_comment_quote')
    sender_comment = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sender_comment')
    receiver_comment = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='receiver_comment')

    def __str__(self):
        return self.content


class ProfileLike(models.Model):
    sender_like = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sender_like')
    receiver_like = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='receiver_like')

    def __str__(self):
        return str(self.id)


class ProfileFavorite(models.Model):
    sender_favorite = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sender_favorite')
    receiver_favorite = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='receiver_favorite')

    def __str__(self):
        return str(self.id)


class VerificationCode(models.Model):
    profile_id = models.OneToOneField(
        Profile, on_delete=models.CASCADE, null=True)
    email_code = models.CharField(max_length=30, blank=True, null=True)
    password_reset_token = models.CharField(
        max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class TeamInvites(models.Model):
    invite_sender = models.ForeignKey(
        Profile, null=True, on_delete=models.CASCADE, related_name='invite_sender')
    invite_receiver = models.ForeignKey(
        Profile, null=True, on_delete=models.CASCADE, related_name='invite_receiver')
    STATUS_CHOICES = [
        ('AWAITING', 'Ожидает'),
        ('ACCEPTED', 'Принят'),
        ('REJECTED', 'Отклонен'),
    ]
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='AWAITING')

    def __str__(self):
        return str(self.id)


class Notifications(models.Model):
    date = models.DateTimeField(default=timezone.localtime)
    sender_profile = models.ForeignKey(
        Profile, blank=True, on_delete=models.CASCADE, related_name='notify_sender_profile')
    receiver_profile = models.ForeignKey(
        Profile, blank=True, on_delete=models.CASCADE, related_name='notify_receiver_profile')
    TYPE_CHOICES = [
        ('NEW_SESSION_LIKE', 'новый лайк фотосессии'),
        ('NEW_SESSION_COMMENT', 'новый комментарий к фотосессии'),
        ('NEW_SESSION_FAVORITE', 'новое добавление фотосессии в избранное'),
        ('NEW_PHOTO_LIKE', 'новый лайк фотографии'),
        ('NEW_PHOTO_COMMENT', 'новый комментарий к фотографии'),
        ('NEW_PHOTO_FAVORITE', 'новое добавление фотографии в избранное'),
        ('NEW_PLACE_LIKE', 'новый лайк места для съемки'),
        ('NEW_PLACE_COMMENT', 'новый комментарий к месту для съемки'),
        ('NEW_PLACE_FAVORITE', 'новое добавление места для съемки в избранное'),
        ('NEW_TRAINING_LIKE', 'новый лайк обучения'),
        ('NEW_TRAINING_COMMENT', 'новый комментарий к обучению'),
        ('NEW_TRAINING_FAVORITE', 'новое добавление обучения в избранное'),
        ('NEW_MESSAGE', 'новое сообщение'),
        ('NEW_FILMING_REQUEST', 'новый запрос на съемку'),
        ('NEW_TRAINING_REQUEST', 'новый запрос на обучение'),
        ('NEW_TEAM_REQUEST', 'новый запрос в команду'),
        ('NEW_REVIEW', 'новый отзыв'),
    ]
    type = models.CharField(
        max_length=25, choices=TYPE_CHOICES)
    action_position = models.IntegerField(null=True)
    readen = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
