from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LOGIN, name='login'),
    path('register/', register, name='register'),
    path('logout/', Logut, name='logout'),
    path('Dashboard/', Dashboard, name='Dashboard'),
    path('productlist/', productlist, name='productlist'),
    path('customer/', customer, name='customer'),
    path('addproduct/', addproduct, name='addproduct'),
    path('adddetail/<int:id>/', adddetail, name='add-detail'),
    path('cartlist/', cartlist, name='cartlist'),
    path('orders/', orders, name='orders'),
    path('orderdetail/<int:id>/', orderdetail, name='orderdetail')

]
