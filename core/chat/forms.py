from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


"""
    This is the form for Signing up
"""
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username']