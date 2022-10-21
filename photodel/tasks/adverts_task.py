from photodel.celery import app
from additional_entities.models import Advertisement, CustomSettings


@app.task
def task_update_current_ad():
    current_ad = CustomSettings.objects.all().first().current_ad
    if Advertisement.objects.all().count() == current_ad:
        CustomSettings.objects.update(current_ad=1)
    else:
        CustomSettings.objects.update(
            current_ad=CustomSettings.objects.all().first().current_ad + 1)
