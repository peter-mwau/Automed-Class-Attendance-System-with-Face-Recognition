# from .models import  Lecturer_report
# from django.shortcuts import render, redirect
# from django.http import HttpResponse

# #read data from csv_name and save to database
# def read_csv(csv_name):
#     with open(csv_name,'r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         user_exist = 0
#         for line in myDataList:
#             entry = line.split(',')
#             # print(entry)
#             nameList.append(entry[0])
#             # print(entry[0])
#         for user in nameList:
#             user =  user.replace(" ","_")
#             if user_exist==0:
#                 print("user is found in database")
#                 user_exist = 1
#                 #save to database
#                 name = user
#                 department = entry[1]
#                 category = entry[2]
#                 unit = entry[3]
#                 faculty = entry[4]
#                 date = entry[5]
#                 # print(name)
#                 # print(department)
#                 # print(category)
#                 # print(unit)
#                 # print(faculty)
#                 # print(date)
#                 #save to database
#                 report = Lecturer_report(name=name,department=department,category=category,unit=unit,faculty=faculty,date=date)
#                 report.save()
#                 print("data saved to database")

import csv, sqlite3
from django.shortcuts import render, redirect

def commit_to_db(csv_name):
   connection = sqlite3.connect("project.sqlite3")
   cursor = connection.cursor()

   with open(csv_name, 'r') as file:
    no_records = 0
    for row in file:
        # print(row.split(',')[0])
        # cursor.execute("INSERT INTO reports_lecturer_report VALUES (?, ?, ?, ?, ?, ?, ?)", row.split(','))
        cursor.execute("INSERT INTO reports_lecturer_report (name, department, category, unit, faculty, date, lecturer_id) VALUES (?, ?, ?, ?, ?, ?, ?)", row.split(','))
        connection.commit()
        no_records += 1
   connection.close()
   print('\n{} Records inserted successfully'.format(no_records))
