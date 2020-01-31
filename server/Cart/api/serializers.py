from rest_framework import serializers
from Cart.models import Purchase, PurchaseItem


class PurchaseItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    class Meta:
        model = PurchaseItem
        fields = ['product_id', 'count']


class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        fields = ['created', 'last_updated', 'active', 'items']
