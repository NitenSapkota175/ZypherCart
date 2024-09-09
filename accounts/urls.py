from django.urls import path
from . import views
urlpatterns = [
        path('',views.Home,name="Home"),
        path('register/',views.SignUp,name="register"),
        path('verify/<str:token>', views.Verify,name='verify'),
        path('login/',views.Userlogin,name="login")
        
]