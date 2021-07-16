from django.shortcuts import render
from record.templates import *

def record(request):
    return render(request, 'record.html')



    

