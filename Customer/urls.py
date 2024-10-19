from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home Screen'),
    path('CustomerList', views.customer_list, name='Customer List'),
]
