from django.http import HttpResponse
from django.shortcuts import render


def login_page(request):
    return render(request, 'loginPage.html')


def home(request):
    return render(request, 'home.html')
