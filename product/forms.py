from django import forms
from django.forms import ModelForm
from .models import *
from tinymce.widgets import TinyMCE
from django.forms import inlineformset_factory


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'class':'form-control', 'cols': 80, 'rows': 10}))
    category = forms.ChoiceField(choices=PRODUCT_FOR, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Product
        fields = ("title", "description", "category", "product_img", "price")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'product_img': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }

class ProductDetailForm(forms.ModelForm): 
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    size = forms.ChoiceField(choices=SHOES_SIZE, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = ProductDetail
        fields = ['product', 'size',]

        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Write Degree Name'}),
        }

productdetailformset = inlineformset_factory(Product, ProductDetail, form=ProductDetailForm, extra=1)