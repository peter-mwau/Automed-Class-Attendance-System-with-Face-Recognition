from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Lecturer_report(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100, null=True)
    date = models.DateField(default="2016-09-23")
    lecturer_id = models.IntegerField(null=True)
    

# class Student_report(models.Model):
#     stud_names = models.CharField(max_length=100)
#     reg_no = models.CharField(max_length=100)
#     picture = models.ImageField(upload_to='images')
#     course = models.CharField(max_length=100)
#     cohort = models.CharField(max_length=100)
#     dateofattendance = models.DateField(auto_now=True)