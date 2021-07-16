from django.urls import path
from .views import authentication

urlpatterns= [
    path('autenticacion/', authentication, name= "autenticacion"),
]