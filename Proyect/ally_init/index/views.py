from django.shortcuts import render
from index.templates import *

def index(request):
    return render(request, 'index.html')