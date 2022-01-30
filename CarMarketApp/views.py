from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import User

from django.db import models
from .models import Car
from .tables import CarTable, MyCarTable
from .forms import SignUpForm, AddCarForm


def main_site(request):
    cars = Car.objects.all()
    table = CarTable(cars)
    return render(request, 'CarMarketApp/main_site.html', {'cars_table': table})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'CarMarketApp/signup.html', {'form': form})

def profile(request):
    current_user = request.user
    my_cars = Car.objects.filter(seller_id = current_user.id)
    my_cars_table = MyCarTable(my_cars)
    return render(request, 'CarMarketApp/profile.html', {"my_cars_table": my_cars_table})

def add_post(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)
        if form.is_valid():
            new_car =  form.save(commit = False)
            new_car.seller_id = User.objects.get(pk=request.user.id)
            new_car.save()
            return redirect('profile')
    else:
        form = AddCarForm()
    return render(request, 'CarMarketApp/add_post.html', {'form': form})

def edit_post(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method=='POST':
        form = AddCarForm(request.POST, instance = car)
        if form.is_valid():
            car = form.save()
            return redirect('profile')
    else:
        form = AddCarForm(instance = car)
    return render(request, 'CarMarketApp/edit_post.html', {'form': form, 'pk': pk})

def delete_post(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('profile')

def details(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'CarMarketApp/details.html', {'car': car})

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'CarMarketApp/login.html')

def log_out(request):
    logout(request)
    return redirect('main_site')