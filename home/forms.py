from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    name = forms.CharField(max_length=30, label ='Ad')
    soyad = forms.CharField(max_length=30, label ='soyad')
    email = forms.CharField(max_length=30, label='e-mail')
    password = forms.CharField(max_length=30, label='password')
    class Meta:
        model = User
        fields = ['name', 'soyad', 'email', 'password']