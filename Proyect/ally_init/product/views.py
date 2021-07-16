from django.shortcuts import render
from product.templates import *

def product(request):
    return render(request, 'product.html')
