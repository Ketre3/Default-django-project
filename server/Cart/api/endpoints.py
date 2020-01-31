from django.urls import path
from .api import (
    AllPurchasesView,
    ActivePurchaseView,
    AddItemPurchaseView,
    DeleteItemPurchaseView,
    TotalPurchaseView,
)

app_name = 'cart_api'
urlpatterns = [
    path('all/', AllPurchasesView.as_view(), name='all'),
    path('active/', ActivePurchaseView.as_view(), name='active'),
    path('add/', AddItemPurchaseView.as_view(), name='add'),
    path('delete/', DeleteItemPurchaseView.as_view(), name='delete'),
    path('total/', TotalPurchaseView.as_view(), name='total'),
]
