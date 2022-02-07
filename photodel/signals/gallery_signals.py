from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from gallery.models import Image, Album, Gallery
from services.scale_image_service import scale_image


@receiver(post_init, sender=Image, dispatch_uid="image_post_init")
def post_init_handler(instance, **kwargs):
    """
    Создание переменных для сохранение значения поля перед изменением
    """
    instance.old_photo = instance.photo


@receiver(post_save, sender=Image, dispatch_uid="image_scale_image")
def scale_image_after_save(sender, instance, created, **kwargs):
    """
    Сигнал масштабирование фото в таблице Image
    """
    if created:
        instance.photo = scale_image(instance.photo)
    elif instance.old_photo != instance.photo:
        instance.photo = scale_image(instance.photo)