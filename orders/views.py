from django.shortcuts import render,HttpResponseRedirect,redirect
from . models import Cart,CartItems
from products.models import Product
from accounts.models import Address,Contact
from accounts.forms import AddressForm,ContactForm
from django.db.models import Sum

def CartPage(request):
        cart_items = CartItems.objects.filter(cart__user = request.user)
        total_price = cart_items.aggregate(total=Sum('price'))
        context = {'cartItems' : cart_items , 'total_price' : total_price['total']}
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

def RemoveItems(request,id):
        if request.method == "POST":
           
           product = Product.objects.get(pk=id)
           user_cart = Cart.objects.get(user=request.user)
           cart_item = CartItems.objects.get(cart=user_cart, product=product)
           
            
           if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                    cart_item.save()
           else:
                    cart_item.delete()
        return redirect('/')

def Checkout(request,id):

      if request.method == 'POST':
            
            user = request.user
            address_is_exists = Address.objects.filter(user=user).exists()
            contact_is_exists = Contact.objects.filter(user=user).exists()
          
            if address_is_exists != True:
                    
                    address =   AddressForm()
                    return render(request,'accounts/address.html',{'forms' : address})
                
            if contact_is_exists != True:
                  
                    contact =   ContactForm()
                    return render(request,'accounts/contact.html',{'forms' : contact})


      address = Address.objects.get(user=request.user)
      contact = Contact.objects.get(user=request.user)
      print(address.city)

      
      context = {'address' : address , 'contact' : contact }


      return render(request,'orders/checkout.html',context)