from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def customer_list(request):
    return render(request, 'customer_list.html', {})
