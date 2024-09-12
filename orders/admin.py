from django.contrib import admin
from . models import Cart,CartItems

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','created_at']

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart' , 'product','quantity','price']