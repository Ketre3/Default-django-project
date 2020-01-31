from django.db import models


class Image(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True
    )
    value = models.ImageField(
        upload_to='image/',
        default='image/default-user-profile-picture.png'
    )

    @property
    def url(self):
        return self.value.url

    def __str__(self):
        return self.name
