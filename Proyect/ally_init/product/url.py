from django.urls import path
from .views import product

urlpatterns= [
    path('producto', product, name= "producto"),
]