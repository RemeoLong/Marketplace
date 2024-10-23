from django.urls import path
from . import views

urlpatterns = [
    path('', views.comingsoon, name="ComingSoon"),
    path('home', views.home, name='Home'),
    path('shop', views.shop, name="Shop"),
    path('details', views.detail, name="Detail"),
    path('cart', views.cart, name="Cart"),
    path('checkout', views.checkout, name="Checkout"),
    path('contact', views.contact, name="Contact"),
    path('CustomerList', views.customer_list, name='Customer List'),
]
