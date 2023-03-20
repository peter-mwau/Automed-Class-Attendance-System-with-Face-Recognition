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
    # a date field which accepts "yyyy-mm-dd h-m-s format"
    date = models.CharField(max_length=100)
    lecturer_id = models.IntegerField(null=True)

    @classmethod
    def getLecturerReport(cls,first,second):
        results = cls.objects.get(fname = first, lname = second)
        return results
    

class Student_report(models.Model):
    stud_names = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    # faculty = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    dateofattendance = models.CharField(max_length=100)

    @classmethod
    def getStudentReport(cls,first,second):
        results = cls.objects.get(fname = first, lname = second)
        return results