from django.contrib import admin
from . models import Cart,CartItems,Order,OrderItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','created_at']

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart' , 'product','quantity','price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id' , 'payment_id' , 'payment_method' , 'amount', 'payment_status' , 'created_at' , 'is_paid' , 'razor_pay_signature' ] 


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order' , 'product'  , 'quantity' , 'price','delivery_date']