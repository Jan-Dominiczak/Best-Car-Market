from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.db import models
from .models import Dealer, Car


def main_site(request):
    cars = Car.objects.all()

    return render(request, 'CarMarketApp/main_site.html', {'cars': cars})

def new_user(request):
    return render(request, 'CarMarketApp/register_new_user.html')

def log_in(request):
    return render(request, 'CarMarketApp/auth_user.html')

def log_out(request):
    logout(request)
    return redirect('main_site')