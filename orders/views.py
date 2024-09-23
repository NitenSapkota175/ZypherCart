from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from . models import Cart,CartItems
from products.models import Product
from accounts.models import Address,Contact
from accounts.forms import AddressForm,ContactForm
from django.db.models import Sum
from . models import Order,OrderItem
from core.razor_clients import client
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import logging
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


def Checkout(request, id):
    user = request.user

    address_is_exists = Address.objects.filter(user=user).exists()
    contact_is_exists = Contact.objects.filter(user=user).exists()

    if not address_is_exists:
        address_form = AddressForm()
        return render(request, 'accounts/address.html', {'forms': address_form})

    if not contact_is_exists:
        contact_form = ContactForm()
        return render(request, 'accounts/contact.html', {'forms': contact_form})

    address = Address.objects.get(user=user)
    contact = Contact.objects.get(user=user)
    product = get_object_or_404(Product, pk=id)

    amount_in_paise = int(product.price * Decimal(100))

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        order = Order.objects.create(
            user=user,
            amount=product.price,  # Store price in INR
            payment_method=payment_method,
            payment_status='Pending',
            is_paid=False
        )

        if payment_method in ['ONLINE', 'UPI']:
           
            razorpay_order = client.order.create({
                "amount": amount_in_paise,  
                "currency": "INR",
                "payment_capture": "1"
            })
            order.order_id = razorpay_order['id']  
            order.save()

            OrderItem.objects.create(order=order,product=product,quantity=1,price= product.price)

            context = {
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'razorpay_order_id': razorpay_order['id'],
                'amount': amount_in_paise,  # Pass amount in paise for Razorpay
                'amount_in_rupees': product.price,  # Pass amount in rupees for display
                'order': order,
                'product': product,
                'address': address,
                'contact': contact
            }
            return render(request, 'orders/payment.html', context)

        elif payment_method == 'COD':
            order.payment_status = 'Pending'
            order.save()
            return redirect('order_success', order_id=order.id)

    context = {
        'address': address,
        'contact': contact,
        'product': product
    }
    return render(request, 'orders/checkout.html', context)


logger = logging.getLogger(__name__)

@csrf_exempt
def PaymentSuccessView(request):
    if request.method == "POST":
        try:
            razorpay_payment_id = request.POST.get('razorpay_payment_id')
            razorpay_order_id = request.POST.get('razorpay_order_id')
            razorpay_signature = request.POST.get('razorpay_signature')

            # Verify the payment signature
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            
            client.utility.verify_payment_signature(params_dict)

            # If successful, mark the order as paid
            order = Order.objects.get(order_id=razorpay_order_id)
            order.payment_id = razorpay_payment_id
            order.payment_status = 'Completed'
            order.is_paid = True
            order.razorpay_signature = razorpay_signature
            order.save()

            return render(request, 'orders/success.html', {'order': order})
        except Exception as e:
            logger.info(f"Payment ID: {razorpay_payment_id}, Order ID: {razorpay_order_id}, Signature: {razorpay_signature}")

            logger.error(f"Payment verification failed: {e}")
            return HttpResponseBadRequest("Payment verification failed.")

    return HttpResponseBadRequest("Invalid request method.")


def OrdersDetails(request):
    orders = Order.objects.filter(user=request.user)  
    order_items = OrderItem.objects.filter(order__in=orders) 
    context = {"order_items": order_items}
    return render(request, 'orders/orders_details.html', context)