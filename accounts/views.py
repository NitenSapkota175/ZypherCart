from django.shortcuts import render,HttpResponse
from . forms import SignUpForm
from .models import Profile,User,Address,Contact
from . utils import send_email_token
import uuid
def SignUp(request):

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


def Verify(request,token):
    try : 
        obj = Profile.objects.get(email_token=token)
        obj.is_verified = True
        obj.save()
        return HttpResponse("Your account has been veriied")
    except Exception as e:
        return HttpResponse('Invalid Token')