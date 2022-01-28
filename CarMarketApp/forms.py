from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30, required = False)
    phone_number = forms.CharField(help_text = 'Your phone number will help buyers contact with you')
    email = forms.EmailField(help_text = 'Your e-mail will help buyers contact with you')
    city = forms.CharField(max_length = 30, help_text = "Tell buyers, where can they buy your car")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')