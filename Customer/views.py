from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def shop(request):
    return render(request, 'shop.html', {})


def detail(request):
    return render(request, 'detail.html', {})


def customer_list(request):
    return render(request, 'customer_list.html', {})
