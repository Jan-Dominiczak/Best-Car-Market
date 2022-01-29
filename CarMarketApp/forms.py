from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Car

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30, required = False)
    phone_number = forms.CharField(help_text = 'Your phone number will help buyers contact with you')
    email = forms.EmailField(help_text = 'Your e-mail will help buyers contact with you')
    city = forms.CharField(max_length = 30, help_text = "Tell buyers, where can they buy your car")
    legal_status = forms.CharField(max_length = 30, help_text = "Private seller/Company")
    company_name = forms.CharField(required = False, help_text = "Optional")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'legal_status', 'company_name', 'city', 'phone_number', 'email', 'password1', 'password2')
        

class AddCarForm(forms.ModelForm):
    # def __init__(self, user):
    #     self.seller_id = user
    # description = forms.CharField(max_length = 4000, required = False, help_text = 'Description is optional, but may help you sell your car faster')
    class Meta:
        model = Car
        fields = ('brand', 'model', 'gen', 'year', 'status', 'available', 'price', 'description')