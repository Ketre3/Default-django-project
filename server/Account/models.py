from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    avatar = models.ForeignKey(
        "Image.Image",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
        null=True
    )
    age = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
