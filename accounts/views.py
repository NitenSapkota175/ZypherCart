from django.shortcuts import render,HttpResponse,redirect
from . forms import SignUpForm
from .models import Profile,User,Address,Contact
from . utils import send_email_token
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
import uuid
def SignUp(request):

    if not request.user.is_authenticated: 
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                user =  fm.save(commit=False)
                token = str(uuid.uuid4())
                user.save()
                Profile.objects.create(
                    
                    user=user , 
                    email_token = token    
                )
                
                fl  = send_email_token(fm.cleaned_data.get('email'),token)
                return render(request,'accounts/home.html')
        else:
            fm = SignUpForm()
        return render(request,'accounts/signup.html',{'form' : fm})
    else:
         return redirect('Home')


def Verify(request,token):
    try : 
        obj = Profile.objects.get(email_token=token)
        obj.is_verified = True
        obj.save()
        return HttpResponse("Your account has been veriied")
    except Exception as e:
        return HttpResponse('Invalid Token')
    

def UserLogin(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':
             
             fm = AuthenticationForm(request=request,data=request.POST)
             if fm.is_valid():
                  usrname = fm.cleaned_data.get('username')
                  passwd = fm.cleaned_data.get('password')
                  usr = authenticate(username=usrname,password=passwd)
                  if usr is not None:  
                        login(request,usr)
                        return redirect("Home")
        else:
             fm = AuthenticationForm()
        return render(request,'accounts/login.html',{'form' : fm})
    else:
        return redirect('Home')

def UserLogout(request):
     
     logout(request)
     return redirect('login')