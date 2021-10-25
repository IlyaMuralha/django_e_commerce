from django.shortcuts import render


def home(request):
    return render(request, 'shopapp/home.html')


def product(request):
    return render(request, 'shopapp/product.html')
