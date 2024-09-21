from django.urls import path
from . import views
urlpatterns = [

            path('addtocart/<uuid:id>',views.AddToCart,name='AddToCart'),
            path('cart/',views.CartPage,name="CartPage"),
            path('remove_items/<uuid:id>',views.RemoveItems,name='RemoveItems'),
            path('checkout/<uuid:id>',views.Checkout,name="Checkout"),
            path('payment/success/', views.PaymentSuccessView,name='payment_success')
]
