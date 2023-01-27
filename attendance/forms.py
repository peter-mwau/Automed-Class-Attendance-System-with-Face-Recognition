from dataclasses import field
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from staff.models import Lecturer_detail

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '_all_'
        fields = ['username','email', 'password1', 'password2']