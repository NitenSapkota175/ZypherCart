from django.db import models
from django.contrib.auth.models import User
from products.models import Product 
from django.utils import timezone
from datetime import timedelta, date
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItems(models.Model):
    
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)

class Order(models.Model):

        PAYMENT_METHOD_CHOICES = [
             ('COD' , 'Cash on Deilvery'),
             ('ONLINE' , 'Card Payment'),
             ('UPI' , 'UPI Payment')
             
             ]
    
        
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        order_id = models.CharField(max_length=225,unique=True,blank=True, null=True)
        payment_id = models.CharField(max_length=225,unique=True,blank=True, null=True)
        payment_method = models.CharField(max_length=20,choices=PAYMENT_METHOD_CHOICES,null=True)
        amount = models.DecimalField(max_digits=10,decimal_places=2)
        payment_status = models.CharField(max_length=20,choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
        default='Pending',null=True)
        created_at = models.DateTimeField(default=timezone.now , null=True)
        is_paid = models.BooleanField(default=False)
        razor_pay_signature = models.CharField(max_length=225,blank=True,null=True) 

        
        def __str__(self):
            return f'Order {self.order_id} by {self.user.username}'

class OrderItem(models.Model):
     order = models.ForeignKey(Order,on_delete=models.CASCADE)
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)
     price = models.DecimalField(max_digits=10,decimal_places=2)
     delivery_date = models.DateField(null=True, blank=True)

     def save(self, *args, **kwargs):
       
        if not self.delivery_date:
            self.delivery_date = date.today() + timedelta(days=7)
        super(OrderItem, self).save(*args, **kwargs)