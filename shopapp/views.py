from django.shortcuts import render


def home(request):
    return render(request, 'shopapp/home.html')


def about(request):
    return render(request, 'shopapp/about.html')
