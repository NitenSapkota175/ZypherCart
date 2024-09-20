from django.urls import path
from . import views
urlpatterns = [

            path('addtocart/<uuid:id>',views.AddToCart,name='AddToCart'),
            path('cart/',views.CartPage,name="CartPage"),
            path('remove_items/<uuid:id>',views.RemoveItems,name='RemoveItems'),
            path('checkout',views.Checkout,name="Checkout")
]
