from django.db import models
from tinymce.models import HTMLField
from AdminModule.models import *
# Create your models here.

PRODUCT_FOR = (
        ('MEN', 'MEN'),
        ('WOMEN', 'WOMEN')
    )
class Product(models.Model):
    


    title = models.CharField(max_length=256)
    description = HTMLField()
    category = models.CharField(choices=PRODUCT_FOR, max_length=25)
    product_img = models.ImageField(upload_to='photos')
    price = models.IntegerField(null=True, blank=True)



SHOES_SIZE = (
        ('7' , '7'),
        ('7.5' ,'7.5' ),
        ('8' , '8'),
        ('8.5' ,'8.5' ),
        ('9' , '9'),
        ('9.5' ,'9.5' ),
        ('10' , '10'),
        ('10.5' , '10.5'),
        ('11' , '11'),
        ('11.5' , '11.5'),
        ('12' , '12'),
        ('13' , '13'),

    )
class ProductDetail(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=25, choices=SHOES_SIZE)


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Address(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=25)
    contact = models.IntegerField()



STATUS_CHOICE = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the way'),
    ('Delivered','Delivered'),
    ('Cancel', 'Cancel')
)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    oder_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICE, default='Pending', max_length=50)