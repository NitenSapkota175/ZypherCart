from django.shortcuts import render, HttpResponse, redirect
from .models import Profile, User, Address, Contact
from .utils import send_email_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . forms import AddressForm,ContactForm,SignUpForm
import logging
import uuid


def SignUp(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                user = fm.save(commit=False)
                token = str(uuid.uuid4())
                email = fm.cleaned_data.get("email")

                user_obj = User.objects.filter(email=email).exists()
                print(user_obj)
                if user_obj == False:
                    
                    user.save()
                    Profile.objects.get_or_create(user=user, email_token=token)

                    send_mail(
                        "Your account needs to be verified",
                        f"Click on the link to verify your account: http://127.0.0.1:8000/accounts/verify/{token}",
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )

                    # send_email_token(email,token)  # not working
                    messages.success(
                        request, "Check your email and verified your account "
                    )
                    return render(request, "accounts/login.html")
        else:
            fm = SignUpForm()
        return render(request, "accounts/signup.html", {"form": fm})
    else:
        return redirect("Home")


def Verify(request, token):
    try:
        obj = Profile.objects.get(email_token=token)
        obj.is_verified = True
        obj.save()
        messages.success(request, "You account has been verified please login")
        return render(request, "accounts/login.html")
    except Exception as e:
        return HttpResponse("Invalid Token")


def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":

            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                usrname = fm.cleaned_data.get("username")
                passwd = fm.cleaned_data.get("password")
                usr = authenticate(username=usrname, password=passwd)

                if usr is not None:
                    profile_obj = Profile.objects.get(user=usr)
                    if profile_obj.is_verified:
                        login(request, usr)
                        return redirect("Home")
                    else:
                        fm = AuthenticationForm()
                        messages.error(request, "First verify your account ")
                        return render(request, "accounts/login.html", {"form": fm})
        else:
            fm = AuthenticationForm()
        return render(request, "accounts/login.html", {"form": fm})
    else:
        return redirect("Home")


def UserLogout(request):

    logout(request)
    return redirect("login")



def AddAdress(request):
    
    if request.method == 'POST':
        fm = AddressForm(request.POST)
        if fm.is_valid():
           address =  fm.save(commit=False)
           address.user = request.user
           address.save()
    return redirect('/')



def Contact(request):
    
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
           contact =  fm.save(commit=False)
           contact.user = request.user
           contact.save()
           print("HELLO")
        else:
            print("Hello world")
    return redirect('/')