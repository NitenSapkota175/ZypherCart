from django.shortcuts import render,HttpResponse
from . models import Product,Category


def ProductHome(request):
    
    return HttpResponse("ProductHome")
