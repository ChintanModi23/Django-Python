from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #return HttpResponse("Hello! This is E-Commerce Index page :")
    return render(request, 'ecomapp/index.html')


def shop(request):
    return render(request, 'ecomapp/shop.html')