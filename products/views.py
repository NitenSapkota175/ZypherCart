from django.shortcuts import render,HttpResponse
from . models import Product,Category


def ProductPage(request,id):
    
    product = Product.objects.get(pk=id)
    context = {'product' : product}
    
    return render(request,'products/product.html',product)
