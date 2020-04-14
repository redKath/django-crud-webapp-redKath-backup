from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #add nested namespace and keeps config in one place
        model = User
        fields = ['username','email','password1','password2']