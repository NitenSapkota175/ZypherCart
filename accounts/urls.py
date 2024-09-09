from django.urls import path
from . import views
urlpatterns = [
       
        path('register/',views.SignUp,name="register"),
        path('verify/<str:token>', views.Verify,name='verify'),
        path('login/',views.UserLogin,name="login"),
        path('logout/',views.UserLogout,name='logout')
        
]