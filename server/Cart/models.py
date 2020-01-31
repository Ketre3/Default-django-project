from django.db import models
# from django.db.models import Sum
from functools import reduce
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.functional import cached_property
import datetime
import operator


class Purchase(models.Model):
    user = models.ForeignKey(
        'Account.Account',
        on_delete=models.CASCADE,
        related_name='purchases',
    )
    last_updated = models.DateTimeField(
        auto_now=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    active = models.BooleanField(
        default=True,
    )

    @cached_property
    def cost(self):
        # OPTIMIZE: many sql queries
        return reduce(
                lambda total, item: total+item,
                map(
                    lambda zipped: zipped[0].cost * zipped[1],
                    zip(
                        map(
                            operator.attrgetter("product"),
                            self.items.select_related('product')
                        ),
                        self.items.values_list('count', flat=True)
                    )
                ), 0)

    @cached_property
    def count(self):
        return reduce(
            lambda total, itm: total + itm,
            self.items.values_list("count", flat=True),
            0
        )

    def __str__(self):
        full_name = self.user.get_full_name()
        title = full_name if full_name else self.user.username
        return f'{title} {self.created.strftime("%Y-%m-%d %H:%M")}; active={self.active}'


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'Product.Product',
        on_delete=models.CASCADE
    )
    count = models.IntegerField(
        default=1
    )

    def __str__(self):
        return f"{self.product.name}: {self.count}"


@receiver(post_save, sender=PurchaseItem)
def purchase_update_time(sender, instance, **kwargs):
    instance.purchase.last_updated = datetime.datetime.now()
    instance.purchase.save()
