from django.contrib import admin
from django.urls import path

from authentication.views import authentication
from record.views import record
from index.views import index
from product.views import product
from cart.views import cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', record),
    path('autenticacion/', authentication),
    path('', index),
    path('producto/', product),
    path('carrito/', cart),
]

