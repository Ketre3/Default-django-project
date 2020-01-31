from django.urls import path

from .views import (
    ProductStyleView,
    SearchListView,
    ProductWithProductTypeListView,

    ProductDeleteView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailView,
)

app_name = 'product'
urlpatterns = [
    path('index/', ProductStyleView.as_view(), name='all'),
    path('search/', SearchListView.as_view(), name='search'),

    path('', ProductWithProductTypeListView.as_view(), name='all-with-type'),

    # CRUD style
    path('<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
]
