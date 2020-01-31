from django.db import models
from django.urls import reverse


class ProductTrend(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    def __str__(self):
        return self.name


class ProductStyle(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ForeignKey(
        'Image.Image',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    product_type = models.ForeignKey(
        'ProductType',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    style = models.ForeignKey(
        'ProductStyle',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    trend = models.ForeignKey(
        'ProductTrend',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    color = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def get_absolute_url(self):
        return reverse("product:detail", args=[self.id])

    def __str__(self):
        return self.name
