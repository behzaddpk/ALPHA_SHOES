from django.shortcuts import render, redirect
from .EmailBackEnd import *
from .models import *
from product.models import *
from product.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def LOGIN(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'),)
        if user:
            login(request, user)
            user = user.user
            if user == 'Admin':
                return redirect('Dashboard')
            else:
                return redirect('/')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = CustomUser(
            email=email, 
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'register.html')


@login_required
def Dashboard(request):
    return render(request, 'Dashboard.html')


@login_required
def customer(request):
    users = Address.objects.all()

    context = {
        'users': users
    }
    return render(request, 'customer.html', context)

@login_required
def cartlist(request):
    cart = Cart.objects.all()

    context = {
        'cart': cart
    }
    return render(request, 'cartlist.html', context)


@login_required
def productlist(request):
    product = Product.objects.all()

    context = {
        'product': product
    }
    return render(request, 'productlist.html', context)


@login_required
def adddetail(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST' and request.POST.get('add_product_detail', False):
        productdetail_formset = productdetailformset(request.POST, instance=product)
        if productdetail_formset.is_valid():
            if product:
                product.save()
            for form in productdetail_formset:
                product = form.cleaned_data['product']
                size = form.cleaned_data['size']
                if form.has_changed():
                    form.instance.product = product
                    form.save()
            
            productdetail_formset = productdetailformset()
    else:
        productdetail_formset = productdetailformset()

    
    context = {
        'productdetail': productdetail_formset,
        'product': product
    }


    
    return render(request, 'add-detail.html', context)


@login_required
def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            product_img = form.cleaned_data['product_img']
            price = form.cleaned_data['price']

            product = Product(title=title, description=description, category=category, product_img=product_img, price=price)
            product.save()
            messages.success(request,'Product Add Successfully')
            form = ProductForm()

    else:
        form = ProductForm()


    context = {
        'form': form
    }
    return render(request, 'addproduct.html', context)


@login_required
def orders(request):
    order = Order.objects.all()

    context = {
        'order': order
    }
    return render(request, 'orders.html', context)


@login_required
def orderdetail(request, id):
    order = Order.objects.get(id=id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        order.status = status
        order.save()
        messages.success(request, 'Order status updated successfully.')


    context = {
        'order': order
    }
    return render(request, 'orderdetail.html', context)

def Logut(request):
    logout(request)
    return redirect('/')