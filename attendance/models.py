from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Student_detail(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images')
    course = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    dateofreg = models.DateField(default='e.g 2021-09-12')
    units = models.CharField(max_length=99)
    faculty = models.CharField(max_length=100, default='e.g CIT')
    category = models.CharField(max_length=100,default='Student')

# return datetime.datetime.fromisoformat(value.toString())

    @classmethod
    def getStudent(cls,first,second):
        results = cls.objects.get(fname = first, lname = second)
        return results