from Product.models import (
    Product,
    ProductStyle,
    ProductType,
)
from django.shortcuts import render
from django.views.generic import ListView, View


class ProductStyleView(View):
    HYPE_STYLE = 'Modern'

    def get(self, request, *args, **kwargs):
        products = Product.objects \
                          .select_related("image") \
                          .filter(style__name=self.HYPE_STYLE)[:5]
        context = {
            "products": products,
            "style": self.HYPE_STYLE,
        }
        return render(request, 'index.html', context)


class SearchListView(ListView):
    model = Product
    allow_empty = True
    context_object_name = 'res_list'
    template_name = 'search.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            query = self.model.objects.filter(name__icontains=search)
        else:
            query = self.model.objects.all()
        return query


class ProductWithProductTypeListView(ListView):
    model = Product
    allow_empty = True
    context_object_name = 'products'
    template_name = 'products.html'

    def get_queryset(self):
        catalog = self.request.GET.get('catalog')
        if not catalog:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(product_type__name=catalog)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['catalogs'] = ProductType.objects.all()
        return context
