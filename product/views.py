from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    product = Product.objects.all()

    context = {
        'product': product
    }
    return render(request, 'index.html', context)


def productdetail(request, id):
    product = Product.objects.get(id=id)
    productdetail = ProductDetail.objects.filter(product=product)

    context = {
        'product': product,
        'productdetail': productdetail
    }
    return render(request, 'product-detail.html', context)

@login_required
def add_to_cart(request):
    user = request.user 
    product = request.GET.get('product')
    size = request.GET.get('prod_size')
    quantity = request.GET.get('quantity')

    
    productdetail = ProductDetail.objects.get(product=product, size=size)
    cart = Cart(user=user, product=productdetail, quantity=quantity)
    cart.save()
    
    return redirect('/cart')
    


@login_required
def cart(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    total_per_item = []  # Create an empty list to store individual item totals
    Initialprice = 0.00
    deliveryprice = 50.00
    amount = 0.00

    cartitem = Cart.objects.filter(user=user)
    if cartitem:
        for cart in cartitem:
            total_price = cart.quantity * cart.product.product.price  # Calculate the total price
            Initialprice += total_price
            total_per_item.append(total_price)  # Append the individual item total to the list
        amount = Initialprice + deliveryprice

    context = {
        'carts': carts,
        'cartitem': cartitem,
        'Initialprice': Initialprice,
        'deliveryprice': deliveryprice,
        'total_per_item': total_per_item,  # Pass the list of item totals to the template
        'amount': amount
    }
    return render(request, 'cart.html', context)




@login_required
def DelProduct(request, id):
    user = request.user
    cart = Cart.objects.get(user=request.user, id=id)
    cart.delete()
    return redirect('cart')


@login_required
def checkout(request):
    user = request.user 
    cart = Cart.objects.filter(user=user)
    address = Address.objects.filter(user=user)

    carts = Cart.objects.filter(user=user)
    total_per_item = []  # Create an empty list to store individual item totals
    Initialprice = 0.00
    deliveryprice = 50.00
    amount = 0.00

    cartitem = Cart.objects.filter(user=user)
    if cartitem:
        for cart in cartitem:
            total_price = cart.quantity * cart.product.product.price  # Calculate the total price
            Initialprice += total_price
            total_per_item.append(total_price)  # Append the individual item total to the list
        amount = Initialprice + deliveryprice


        context = {
            'cart':cart,
            'cartitem': cartitem,
            'Initialprice': Initialprice,
            'deliveryprice': deliveryprice,
            'total_per_item': total_per_item,  # Pass the list of item totals to the template
            'amount': amount,
            'address': address
        }
        return render(request, 'checkout.html', context)
    else:
        return render(request, 'emptycheckout.html')

@login_required
def address(request):
    user = request.user
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        state = request.POST.get('state')
        contact = request.POST.get('contact')
        print(fname, lname, address, state, contact)
        

        address = Address(user=user, fname=fname, lname=lname, address=address, state=state, contact=contact)
        address.save()
        messages.success(request, 'Address has been saved')
        return redirect('checkout')

@login_required
def CompleteOrder(request):
    user = request.user
    ad_id = request.GET.get('address')
    address = Address.objects.get(id=ad_id)
    cart = Cart.objects.filter(user=user)

    for c in cart:
        # Create a new Order instance and set the cart_id
        order = Order(
            user=user,
            address=address,
            product=c.product,
        )
        order.save()
        print('Your order complete')
        c.delete()
        print('your data delete')

    return redirect('order')


@login_required
def order(request):
    user = request.user
    order = Order.objects.filter(user=user)

    context = {
        'order':order
    }
    return render(request, 'order.html', context)



def about(request):
    return render(request, 'about.html')


def Men(request):
    product = Product.objects.filter(category='MEN')

    context = {
        'product': product
    }
    return render(request, 'men.html', context)


def Women(request):
    product = Product.objects.filter(category='WOMEN')

    context = {
        'product':product
    }
    return render(request, 'women.html', context)