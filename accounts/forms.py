from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Address,Contact
from phonenumber_field.modelfields import PhoneNumberField
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' ,'first_name','last_name'  ,'email' ]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country', 'city', 'state', 'street_address', 'pincode']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}),
            'street_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your street address'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pincode'}),
        }

class ContactForm(forms.ModelForm):


    class Meta:
        model = Contact
        fields = ['phone_number', 'secondary_email']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'}),
            'secondary_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your secondary email'}),
        }