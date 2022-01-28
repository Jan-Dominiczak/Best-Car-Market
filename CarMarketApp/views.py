from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from .models import Dealer, Car
from .tables import CarTable
from .forms import SignUpForm


def main_site(request):
    cars = Car.objects.all()
    table_class = CarTable(cars)
    return render(request, 'CarMarketApp/main_site.html', {'cars_table': table_class})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('edit_profile')
    else:
        form = SignUpForm()
    return render(request, 'CarMarketApp/signup.html', {'form': form})

def edit_profile(request):
    return render(request, 'CarMarketApp/edit_profile.html')

def log_in(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     return redirect('main_site')
    return render(request, 'CarMarketApp/auth_user.html')

def log_out(request):
    logout(request)
    return redirect('main_site')