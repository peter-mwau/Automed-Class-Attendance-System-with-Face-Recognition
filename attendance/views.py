import email
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.forms import BaseInlineFormSet_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# from django.contrib.auth import  authenticate
# from django. contrib import auth

from django.contrib import messages
import datetime

from multiprocessing import context
from xml.etree.ElementInclude import include
from django import views, forms
from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateUserForm, selectCameraForm

from attendance.recognize import runFile

from staff.models import Lecturer_detail
from . models import Student_detail
from reports.models import Lecturer_report, Student_report
from django.template import loader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from reports.recognize import runFile

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.info(request, ('Incorrect username or password!!'))
            return redirect('login_user')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, ('You have been logged out!!'))
    return redirect('login_user')


# @csrf_exempt
# def camera(request):
#     form = selectCameraForm(initial={'camera': '0'})


#     # if request.method == 'POST':
#     #     form = selectCameraForm(request.POST)
#     #     if form.is_valid():
            
#     #         # get the value of the selected camera
#     #         camera = form.cleaned_data.get('camera')
#     #         if camera == '0':
#     #             camera = 'Webcam'
#     #         else:
#     #             camera = 'External Camera'
#             # subm
            
                
            
#             # form.save()
#             # messages.success(request, 'Camera selected' + camera)
#             # form = selectCameraForm(initial={'camera': camera})
#             # return render(request, 'home.html', {'form': form})
#     # else:
#         # form = selectCameraForm(initial={'camera': '0'})
#     return render(request, 'home.html', {'form': form})   

    
def home(request):
    # context = {}
    # form = selectCameraForm(initial={'camera': '0'})
    # if request.method == 'POST':
    #     form = selectCameraForm(request.POST)
    #     if form.is_valid():
            
    #         # get the value of the selected camera
    #         camera = form.cleaned_data.get('camera')
    #         if camera == '0':
    #             camera = 0
    #         else:
    #             camera = 1
    #         print(camera)
            # redirect to capture with camera as parameter
            # return redirect('reports', camera) 

    #  select from the students report table where the dateofattendance is today interms of datetime
    today_student_attendance = Student_report.objects.filter(dateofattendance=datetime.date.today())
    # print(today_student_attendance)  
    # to print today's date in the format of year-month-day-hour-minute-second
    # print(datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")) 
    # get the total number of students whose attendance has been taken today
    today_students = today_student_attendance.count()
    # print(today_students)
    # select from the lecturers report table where the dateofattendance is today
    today_lecturer_attendance = Lecturer_report.objects.filter(date=datetime.date.today())
    # get the total number of lecturers whose attendance has been taken today
    today_lecturers = today_lecturer_attendance.count()
    today_attendance = today_lecturers + today_students

    # select from the students report table where the dateofattendance is last seven days
    last_seven_days_student_attendance = Student_report.objects.filter(dateofattendance__range=[datetime.date.today() - datetime.timedelta(days=7), datetime.date.today()])
    # get the total number of students whose attendance has been taken in the last seven days
    last_seven_days_students = last_seven_days_student_attendance.count()
    # select from the lecturers report table where the dateofattendance is last seven days
    last_seven_days_lecturer_attendance = Lecturer_report.objects.filter(date__range=[datetime.date.today() - datetime.timedelta(days=7), datetime.date.today()])
    # get the total number of lecturers whose attendance has been taken in the last seven days
    last_seven_days_lecturers = last_seven_days_lecturer_attendance.count()
    week_attendance = last_seven_days_lecturers + last_seven_days_students

    # get total number of students in the Student_detail table
    total_students = Student_report.objects.count()
    total_lecturers = Lecturer_report.objects.count()
    total_attendance = total_lecturers + total_students
    # get first_name and last_name from auth_user table and destructure user
    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    # concantinate first_name and last_name
    name = first_name +" "+ last_name

    # if user is logged in get the details of the user if the category is either lecturer or student
    if user.is_authenticated:
        name = user.first_name +" "+ user.last_name
        # get fname and last name from the Lecturer_detail table
        stuDetails = Student_detail.objects.all()
        stuDetails = stuDetails[0]
        lecDetails = Lecturer_detail.objects.all()
        lecDetails = lecDetails[0]
        fname = stuDetails.fname
        lname = stuDetails.lname
        full_name = fname +" "+ lname
        firstName = lecDetails.fname
        lastName = lecDetails.lname
        fullName = firstName +" "+ lastName
        if full_name==name:
            dict = [{
                'studName': stuDetails.fname +" "+ stuDetails.lname,
                'picture': stuDetails.picture,
                'course': stuDetails.course,
                'reg_no': stuDetails.reg_no,
                'cohort': stuDetails.cohort,
                'category': stuDetails.category,
                'units': stuDetails.units,
                'faculty': stuDetails.faculty,
                'dateofreg': stuDetails.dateofreg,
            }]
        elif fullName == name:
            dict = [{
                'lecName': lecDetails.fname +" "+ lecDetails.lname,
                'image': lecDetails.image,
                'lecturer_id': lecDetails.lecturer_id,
                'units_teaching': lecDetails.units_teaching,
                'faculty': lecDetails.faculty,
                'category': lecDetails.category,
                'department': lecDetails.department,
                'dateofreg': lecDetails.dateofreg,
            }]
        else:
            dict = [{
                'username': user.username,
                'email': user.email,
                'category': 'Admin',
                'first_name': user.first_name,
                'last_name': user.last_name,
                'date_joined': user.date_joined,
            }]
    else:
        dict = [{
            'username': 'Guest',
            'email': 'Guest',
            'category': 'Guest',
            'first_name': 'Guest',
            'last_name': 'Guest',
            'date_joined': 'Guest',
        }]
    
    context = {'name':name, 'total_students':total_students, 'total_lecturers':total_lecturers, 'total_attendance':total_attendance,'today_lecturers':today_lecturers,'today_students':today_students, 'today_attendance':today_attendance,'week_lec_attendance':last_seven_days_lecturers,'week_stud_attendance':last_seven_days_students, 'week_attendance':week_attendance,'dict':dict}
    return render(request, 'dashboard.html', context)


def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Account was created for ' + username)
            # return render(request, 'login.html')
            return redirect('login_user')
        # else:
        #     messages.info(request, ('Incorrect username or password!!'))
        #     return redirect('register_user')
    else:
        form = CreateUserForm()

        # password for account 'punisher':'punisherdefrgthuj'
        # password for account 'hamisimahamud':'lkjhgfdsa123'
        # password for account 'Cristiano_Ronaldo':'zxcvbnmmnbvcxz'
        # password for account 'thegoat_mwenyewe': 'asdfghjkllkjhgfdsa'
        # password for account 'johnsmith': 'qwertyuioppoiuytrewq'

    context = {'form': form}
    return render(request, 'register.html', context)

def reports(request):
    runFile() 
    return render(request, 'capture.html', context)

def capture(request):
    context={}
    return render(request, 'capture.html', context)


























    # student = Student_detail.objects.all()
    # # destructure student
    # fname = student.first_name
    # lname = student.last_name
    # # get first_name and last_name from auth_user table
    # user = request.user
    # # destructure user into first_name and last_name
    # first_name = user.first_name
    # last_name = user.last_name
    # # compare first_name and last_name from auth_user table with first_name and last_name from student_detail table
    # if fname == first_name and lname == last_name:
    #     # query all the data from student_detail table
    #     student = Student_detail.objects.all()
    #     # destructure student
    #     fname = student.first_name
    #     lname = student.last_name
    #     regno = student.regno
    #     course = student.course
    #     picture = student.picture
    #     dateofreg = student.dateofreg
    #     units = student.units
    #     faculty = student.faculty
    #     category = student.category
    #     context = {'student': student, 'fname': fname, 'lname': lname, 'regno': regno, 'course': course, 'picture': picture, 'dateofreg': dateofreg, 'units': units, 'faculty': faculty, 'category': category}
    #     return render(request, 'dashboard.html', context)
    # else:
    #     context = {'student': student}
    #     return render(request, 'dashboard.html', context)
    
  




