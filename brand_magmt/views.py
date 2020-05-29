from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'brand/index.html')


def dashboard(request):
    return render(request, 'brand/dashboard.html')


def products(request):
    return render(request, 'brand/products.html')


def designers(request):
    return render(request, 'brand/designers.html')


def requests(request):
    return render(request, 'brand/requests.html')


def settings(request):
    return render(request, 'brand/settings.html')


def market(request):
    return render(request, 'brand/market.html')


def register(request):
    return render(request, 'brand/register.html')


def profile(request):
    return render(request, 'brand/profile.html')


def dregister(request):
    return render(request, 'brand/dregister.html')