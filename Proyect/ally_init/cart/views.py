from django.shortcuts import render
from cart.templates import *

def cart(request):
    return render(request, 'cart.html')
