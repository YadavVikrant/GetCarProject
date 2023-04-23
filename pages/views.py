from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def Home(request):
    return render(request,'pages/index.html')
