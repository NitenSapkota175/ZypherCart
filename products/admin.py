from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name', 'category_desc']
    


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'product_desc', 'price', 'category']
   
