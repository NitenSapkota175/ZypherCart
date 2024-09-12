from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product,Category
@login_required
def Home(request):
    products = Product.objects.all()
    
    context = {'products' : products}    
    return render(request,'core/home.html',context)