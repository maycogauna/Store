from django.urls import path
from .views import record


urlpatterns= [
    path('registro/', record, name= "registro"),
]
