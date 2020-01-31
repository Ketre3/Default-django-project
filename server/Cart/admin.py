from django.contrib import admin
from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["user", "created", "active", "cost", "count"]
    list_filter = ["user", "created"]
