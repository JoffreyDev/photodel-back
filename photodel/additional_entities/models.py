from django.db import models


class EmailFragment(models.Model):
    verify_email = models.TextField(null=True)
    reset_password = models.TextField(null=True)