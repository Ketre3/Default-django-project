from django.urls import path
from .views import (
    cart_view,
    purchase_confirm_view,
)

app_name = 'cart'
urlpatterns = [
    path('', cart_view, name='cart'),
    path('confirm/', purchase_confirm_view, name='confirm'),
]
