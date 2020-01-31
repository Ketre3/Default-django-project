from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from django.db.models import F
from rest_framework.views import APIView
from .serializers import PurchaseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from Product.models import Product
from Product.serializers import ProductSerializer
import operator
from django.shortcuts import get_object_or_404


class AllPurchasesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        user = self.request.user
        return user.purchases.all()


class ActivePurchaseView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = PurchaseSerializer

    def get(self, request, format=None):
        user = request.user
        current_purchase, _ = user.purchases.get_or_create(active=True)
        serializer = PurchaseSerializer(current_purchase)
        return Response(serializer.data)


class AddItemPurchaseView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request, format=None):
        product_id = request.data['id']
        count = request.data['count']
        user = request.user
        purchase, _ = user.purchases.get_or_create(active=True)
        item = purchase.items.filter(product_id=product_id).first()
        if item:
            item_count = item.count + count
            item.count = item_count
            item.save()
        else:
            # first item in purchase
            product = get_object_or_404(Product, id=product_id)
            item = purchase.items.create(product=product, count=count)
            item_count = 1
        return Response({"status": "ok"})


class DeleteItemPurchaseView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request, format=None):
        product_id = request.data['id']
        count = request.data['count']
        user = request.user
        purchase, _ = user.purchases.get_or_create(active=True)
        item = purchase.items.filter(product_id=product_id).first()
        if item:
            item_count = item.count - count
            if item_count < 0:
                item.delete()
                item_count = 0
            else:
                item.count = item_count
                item.save()

        return Response({"status": "ok"})


class TotalPurchaseView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request, format=None):
        user = request.user
        purchase, _ = user.purchases.get_or_create(active=True)
        items = [ProductSerializer(
                                product, context={"count": float(count)}
                            ).data
                for product, count in zip(
                            # product
                            map(operator.attrgetter("product"),
                                purchase.items.select_related('product')),
                            # count
                            purchase.items.values_list('count', flat=True)
                )]
        return Response(items)

    def post(self, request, format=None):
        user = request.user
        purchase = user.purchases.get(active=True)
        # some confirm-payment stuff should be here.
        # ...
        purchase.active = False
        purchase.save()
        return Response({"status": "ok"})
