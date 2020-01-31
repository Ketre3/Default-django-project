import datetime
from django.contrib import admin
from .models import Product, ProductTrend, ProductStyle, ProductType
from django.template.loader import render_to_string


@admin.register(Product)
class ProdAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'product_type', 'picture', 'cost',
        'modified', 'created', 'is_new'
    ]
    list_filter = [
        'product_type', 'created'
    ]
    search_fields = [
        'title', 'product_type'
    ]
    fieldsets = (
        (
            None, {
                'fields': ('name', 'description')
            }
        ),
        (
            'properties', {
                'fields': ('product_type' ,'image', 'style', 'trend')
            }
        ),
        (
            'Other', {
                'fields': ('color', 'cost')
            }
        )
    )

    def picture(self, obj):
        return render_to_string(
            'base/image_admin.html',
            {'image': obj.image.url}
        )

    def is_new(self, obj):
        today = datetime.datetime.now()
        return True if obj.created.date() >= today.date() else False


admin.site.register(ProductType)
admin.site.register(ProductTrend)
admin.site.register(ProductStyle)
