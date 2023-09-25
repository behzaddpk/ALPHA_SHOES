from django.contrib import admin
from .models import *
# Register your models here.



class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDetailInline]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']


admin.site.register(Address)
admin.site.register(Order)
