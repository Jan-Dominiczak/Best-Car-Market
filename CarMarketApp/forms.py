from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Car, Contact

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30, required = False)
    email = forms.EmailField(help_text = 'Your e-mail will help buyers contact with you')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
class AddContactForm(forms.ModelForm):
    company_name = forms.CharField(max_length = 50, required = False, help_text = 'Optional')
    class Meta:
        model = Contact
        fields = ('phone_number', 'city', 'seller_status', 'company_name')

class AddCarForm(forms.ModelForm):
    # def __init__(self, user):
    #     self.seller_id = user
    # description = forms.CharField(max_length = 4000, required = False, help_text = 'Description is optional, but may help you sell your car faster')
    class Meta:
        model = Car
        fields = ('brand', 'model', 'gen', 'year', 'status', 'available', 'price', 'description')