from collections import UserDict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import user

class CreateUserForm(UserCreationForm):
    class Meta:
        model=UserDict
        fields=['username', 'email', 'password1', 'password2']