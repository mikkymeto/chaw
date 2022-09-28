
from django.contrib import admin
from .models import Payment, Shopcart

# Register your models here.


@admin.register(Shopcart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['user','dish','c_name','quantity','c_price','amount', 'cart_code', 'paid']
    readonly_fields = ('user', 'dish', 'c_name', 'quantity','c_price', 'amount', 'cart_code', 'paid')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','total','cart_code','pay_code','paid','pay_date','admin_note', 'admin_update')
    readonly_fields = ('user', 'first_name', 'last_name', 'total','cart_code', 'pay_code', 'paid', 'pay_date')