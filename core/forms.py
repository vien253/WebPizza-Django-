from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
class SignUpForm(UserCreationForm):
    class Meta:
        model = AbstractUser
        fields= ('username','password1','password2', 'email')