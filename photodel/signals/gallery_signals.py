from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from gallery.models import Image
from services.scale_image_service import scale_image


@receiver(post_init, sender=Image)
def post_init_handler(instance, **kwargs):
    """
    Создание переменных для сохранение значения поля перед изменением
    """
    instance.old_photo = instance.photo


@receiver(post_save, sender=Image)
def scale_image_after_save(sender, instance, created, **kwargs):
    """
    """
    if instance.old_photo != instance.photo:
        instance.photo = scale_image(instance.photo)