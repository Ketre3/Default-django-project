from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(source='image.url')
    url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_count(self, obj):
        return self.context.get("count", 1.0)

    def get_total(self, obj):
        return float(obj.cost) * self.context.get("count", 1.0)

    class Meta:
        model = Product
        fields = ['id', 'url', 'name', 'count',
                  'cost', 'image_url', 'total']
