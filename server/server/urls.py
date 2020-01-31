from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include, reverse_lazy
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
api_urls = [
    path('cart/', include('Cart.api.endpoints', 'cart_api')),
] # + router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('Product.urls', 'product')),
    path('cart/', include('Cart.urls', 'cart')),
    path('account/', include("Account.urls", 'account')),

    path('api/', include(api_urls)),

    path('', RedirectView.as_view(url=reverse_lazy('product:all'))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from debug_toolbar import urls as debug_urls
    urlpatterns += [path('__debug__/', include(debug_urls))]
