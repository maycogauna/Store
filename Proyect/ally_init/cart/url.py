from django.urls import path
from .views import cart


urlpatterns= [
    path('carrito/', cart, name= "carrito"),
]