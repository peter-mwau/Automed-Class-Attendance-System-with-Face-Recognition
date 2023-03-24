from .models import  Lecturer_report, Student_report
from django.shortcuts import render, redirect
from django.http import HttpResponse


# #read data from csv_name and save to database
def read_csv(csv_name):
    with open(csv_name, 'r') as file:
        no_records = 0
        for row in file:
            print(row.split(',')[0])
            Lecturer_report.objects.create(name=row.split(',')[0], category=row.split(',')[1], date=row.split(',')[2], department=row.split(',')[3], faculty=row.split(',')[4], unit=row.split(',')[5], lecturer_id=row.split(',')[6])
            no_records += 1
    print('\n{} Records inserted successfully'.format(no_records))

# read data from csv_name and save to student report table in database
def read_csv2(csv_name):
    with open(csv_name, 'r') as file:
        no_records = 0
        for row in file:
            print(row.split(',')[0])
            Student_report.objects.create(stud_names=row.split(',')[0], reg_no=row.split(',')[1], course=row.split(',')[2], cohort=row.split(',')[3], category=row.split(',')[4], unit=row.split(',')[5], dateofattendance=row.split(',')[6])
            no_records += 1
    print('\n{} Records inserted successfully'.format(no_records))








  
