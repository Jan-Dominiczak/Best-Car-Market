from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import User
from django_tables2 import RequestConfig
from django.contrib import messages

from django.db import models
from .models import Car, Contact
from .tables import CarTable, MyCarTable
from .forms import SignUpForm, AddCarForm, AddContactForm


def main_site(request):
    cars = Car.objects.all()
    table = CarTable(cars)
    RequestConfig(request).configure(table)
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
            my_info = Contact(city = ' ',phone_number = int() , seller_status = ' ', company_name = ' ', user_id = User.objects.get(pk=request.user.id))
            my_info.save()
            return redirect('update_user_contact_info')
    else:
        form = SignUpForm()
    return render(request, 'CarMarketApp/signup.html', {'form': form})

def profile(request):
    current_user = request.user
    my_cars = Car.objects.filter(seller_id = current_user.id)
    my_cars_table = MyCarTable(my_cars)
    RequestConfig(request).configure(my_cars_table)
    return render(request, 'CarMarketApp/profile.html', {"my_cars_table": my_cars_table})

def update_user_contact_info(request):
    user_contact = Contact.objects.get(user_id = request.user)
    if request.method =='POST':
        form = AddContactForm(request.POST, instance = user_contact)
        if form.is_valid():
            user_contact = form.save(commit=False)
            user_contact.save()
            return redirect('profile')
    else:
        form = AddContactForm(instance = user_contact)
    return render(request, 'CarMarketApp/update_user_contact_info.html', {'form': form})

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
    current_user = request.user
    if car.seller_id == User.objects.get(pk=current_user.id):
        if request.method=='POST':
            form = AddCarForm(request.POST, instance = car)
            if form.is_valid():
                car = form.save()
                return redirect('profile')
        else:
            form = AddCarForm(instance = car)
    else:
        return redirect('er_auth')
    return render(request, 'CarMarketApp/edit_post.html', {'form': form, 'pk': pk})

def delete_post(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('profile')

def details(request, pk):
    car = get_object_or_404(Car, pk=pk)
    contact = Contact.objects.get(user_id = car.seller_id.pk)
    return render(request, 'CarMarketApp/details.html', {'car': car, 'contact': contact})

def er_auth(request):
    return render(request, 'CarMarketApp/er_auth.html')

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Incorrect username OR password')
    return render(request, 'CarMarketApp/login.html')

def log_out(request):
    logout(request)
    return redirect('main_site')