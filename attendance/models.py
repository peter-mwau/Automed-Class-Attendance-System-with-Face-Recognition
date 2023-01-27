from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Student_detail(models.Model):
    stud_names = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images')
    course = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    dateofreg = models.DateField(default='e.g 2021-09-12')
    units = models.CharField(max_length=99)
    faculty = models.CharField(max_length=100, default='e.g CIT')

# return datetime.datetime.fromisoformat(value.toString())