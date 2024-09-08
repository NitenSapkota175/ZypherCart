from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
class Address(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    pincode = models.CharField(max_length=20)


class Contact(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True)
    secondary_email = models.EmailField(blank=True,null=True)