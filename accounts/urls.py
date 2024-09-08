from django.urls import path
from . import views
urlpatterns = [

        path('',views.AccountHome,name="AccountHome"),
]