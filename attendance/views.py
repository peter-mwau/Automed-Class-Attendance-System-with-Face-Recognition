import email
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.forms import BaseInlineFormSet_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from multiprocessing import context
from xml.etree.ElementInclude import include
from django import views, forms
from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateUserForm

from attendance.recognize import runFile

from staff.models import Lecturer_detail
from django.template import loader

# from reports.recognize import runFile

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect email or password ')

    context = {}
    return render(request, 'index.html', context)
    
def home(request):
    context = {}
    return render(request, 'home.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return render('index')

    context = {'form': form}
    return render(request, 'register.html', context)

def reports(request):
    context = {}
    runFile()
    return render(request, 'attendance.csv')




