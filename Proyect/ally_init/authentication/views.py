from django.shortcuts import render
from authentication.templates import *

def authentication(request):
    return render(request,"authentication.html")




    
