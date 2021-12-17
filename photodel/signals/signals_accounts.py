from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from django.contrib.auth.models import User
from accounts.models import Profile, Album


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        Album.objects.create(profile=profile, name_album='Главный')
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=instance)
            Album.objects.create(profile=profile, name_album='Главный')
