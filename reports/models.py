from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Lecturer_report(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    lecturer_id = models.IntegerField()
    dateofattendance = models.DateField(auto_now=True)

class Student_report(models.Model):
    stud_names = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images')
    course = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    dateofattendance = models.DateField(auto_now=True)