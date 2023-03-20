from time import timezone
from django.db import models
from datetime import datetime
from django.utils import timezone
# from recognize import csv_name
import csv

# Create your models here.
class Lecturer_detail(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    lecturer_id = models.IntegerField()
    dateofreg = models.DateField(default='e.g 2016-09-23')
    units_teaching = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='Lecturer')

    @classmethod
    def getLecturer(cls,first,second):
        results = cls.objects.get(fname = first, lname = second)
        return results

    # a method to save data from a csv file to the database

  





            
