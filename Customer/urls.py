from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('shop', views.shop, name='Shop'),
    path('details', views.detail, name="Detail"),
    path('CustomerList', views.customer_list, name='Customer List'),
]
