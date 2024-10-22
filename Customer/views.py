from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def shop(request):
    return render(request, 'shop.html', {})


def detail(request):
    return render(request, 'detail.html', {})


def cart(request):
    return render(request, 'cart.html', {})


def checkout(request):
    return render(request, 'checkout.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def customer_list(request):
    return render(request, 'customer_list.html', {})
