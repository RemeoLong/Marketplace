from django.shortcuts import render


def home(request):
    return render(request, 'Index/home.html', {})


def comingsoon(request):
    return render(request, 'Index/index_comingsoon.html', {})


def shop(request):
    return render(request, 'Index/shop.html', {})


def detail(request):
    return render(request, 'Index/detail.html', {})


def cart(request):
    return render(request, 'Index/cart.html', {})


def checkout(request):
    return render(request, 'Index/checkout.html', {})


def contact(request):
    return render(request, 'Index/contact.html', {})


def customer_list(request):
    return render(request, 'customer_list.html', {})
