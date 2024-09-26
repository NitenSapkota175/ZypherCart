from django.urls import path
from . import views

urlpatterns = [
    path("addtocart/<uuid:id>", views.AddToCart, name="AddToCart"),
    path("cart/", views.CartPage, name="CartPage"),
    path("orders_details/", views.OrdersDetails, name="Orders"),
    path("remove_items/<uuid:id>", views.RemoveItems, name="RemoveItems"),
    path("checkout/<uuid:id>", views.DirectCheckout, name="DirectCheckout"),
    path("cartcheckout/", views.CartCheckout, name="CartCheckout"),
    path("payment/success/", views.PaymentSuccessView, name="payment_success"),
]
