from Product.mixins import AdminGroupRequired
from django.views.generic import (
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from Product.models import (
    Product,
    ProductType,
)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'CRUD/read_product.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['catalogs'] = ProductType.objects.all()
        return context


class ProductCreateView(AdminGroupRequired, CreateView):
    model = Product
    template_name = 'CRUD/create_product.html'
    redirect_url = reverse_lazy('product:all')
    success_url = reverse_lazy('product:all')
    fields = ['name', 'description', 'product_type', 'style',
              'image', 'color', 'cost']


class ProductDeleteView(AdminGroupRequired, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'CRUD/delete_product.html'
    redirect_url = reverse_lazy('product:all')
    success_url = reverse_lazy('product:all')


class ProductUpdateView(AdminGroupRequired, UpdateView):
    model = Product
    template_name = 'CRUD/update_product.html'
    redirect_url = reverse_lazy('product:all')
    success_url = reverse_lazy('product:all')
    fields = ['name', 'description', 'product_type', 'style',
              'image', 'color', 'cost']
