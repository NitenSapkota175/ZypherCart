from django.contrib import admin
from . models import Address,Contact,Profile

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country','city','state','street_address','pincode','user']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number','secondary_email','user']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email_token','is_verified','user']