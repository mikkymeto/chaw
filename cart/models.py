from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from techbro.models import Dish


# Create your models here.

class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    c_item = models.IntegerField(default=1)
    c_date = models.DateTimeField(auto_now_add=True)
    c_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    c_price = models.IntegerField()
    amount = models.IntegerField()
    cart_code = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username


class Meta:
        db_table = 'shopcart'
        managed = True
        verbose_name = 'Shopcart'
        verbose_name_plural = 'Shopcarts'       


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)        
    last_name = models.CharField(max_length=50) 
    total = models.IntegerField()
    cart_code = models.CharField(max_length=255)       
    pay_code = models.CharField(max_length=36)
    phone = models.CharField(max_length=20, default='a') 
    city = models.CharField(max_length=20, default='a')     
    address = models.CharField(max_length=20, default='a')     
    paid = models.BooleanField(default=False)
    pay_date = models.DateTimeField(auto_now_add=True)       
    admin_note = models.CharField(max_length=255)       
    admin_update = models.DateTimeField(auto_now=True)   

    def __str__(self):  
       return self.user.username

    class Meta:
        db_table = 'payment'
        managed = True 
        verbose_name = 'Payments' 
        verbose_name_plural = 'payments'  