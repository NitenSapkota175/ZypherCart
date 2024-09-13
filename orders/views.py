from django.shortcuts import render,HttpResponseRedirect,redirect
from . models import Cart,CartItems
from products.models import Product
from django.db.models import Sum

def CartPage(request):
        cart_items = CartItems.objects.filter(cart__user = request.user)
        total_price = cart_items.aaggregate(total=Sum('price'))
        context = {'cartItems' : cart_items , 'total_price' : total_price}
        return render(request , 'orders/cart.html',context)

def AddToCart(request,id):

    cart_is_exists = Cart.objects.filter(user=request.user).exists()

    if cart_is_exists:
           cart = Cart.objects.get(user=request.user)
                     
    else:
          cart = Cart.objects.create(user=request.user)
    
    
    product = Product.objects.get(pk=id)

    cart_items_is_exists = CartItems.objects.filter(cart=cart,product=product).exists()
    
    if cart_items_is_exists:
        cart_item = CartItems.objects.get(cart=cart,product=product)
        cart_item.quantity +=1 
        cart_item.price += product.price
        cart_item.save()
    else:
         CartItems.objects.create(cart=cart,product=product,quantity=1,price=product.price)

    return redirect('Home')

