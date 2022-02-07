from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from accounts.models import Profile
from gallery.models import Album, Image


@receiver(post_save, sender=User, dispatch_uid="user_create_profile")
def save_or_create_profile(sender, instance, created, **kwargs):
    """
    Сигнал создание профиля и альбома с фото при создании пользователя
    """
    if created:
        profile = Profile.objects.create(user=instance)
        image = Image.objects.filter(profile__user__username='admin').first()
        Album.objects.create(profile=profile, name_album='Разное', main_photo_id=image)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=instance)
            image = Image.objects.filter(profile__user__username='admin').first()
            Album.objects.create(profile=profile, name_album='Разное', main_photo_id=image)