from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from django.contrib.auth.models import User
from accounts.models import Profile


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    """
    При создании юзера автоматическое создание профиля пользователя
    """
    if created:
        profile = Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=instance)
