from django.urls import path
from . import views
urlpatterns = [

        path('',views.ProductHome,name="ProductHome"),
]