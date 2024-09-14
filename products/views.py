from django.shortcuts import render,HttpResponse
from . models import Product,Category


def ProductPage(request,id):
    
    product = Product.objects.get(pk=id)
    category = Product.category
    context = {'product' : product,'category' : category}
    
    return render(request,'products/product.html',context)
