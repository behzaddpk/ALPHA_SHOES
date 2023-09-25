from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('product/<int:id>/', productdetail, name='productdetail'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('DelProduct/<int:id>/', DelProduct, name='DelProduct'),
    path('checkout/', checkout, name='checkout'),
    path('Address/', address, name='address'),
    path('CompleteOrder', CompleteOrder, name='CompleteOrder'),
    path('order/', order, name='order'),
    path('about/', about, name='about'),
    path('Men/', Men, name='Men'),
    path('Women/', Women, name='Women')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)