from time import timezone
from django.db import models
from datetime import datetime
from django.utils import timezone

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



#  A function to create a table in database and commit data from csv file to database with the specified columns
    # @classmethod
    # def create_table(cls, csv_name):
    #     import csv
    #     from attendance import recognize
    #     csv_name = 'attendance.csv'
    #     with open(csv_name, 'r') as f:
    #         reader = csv.reader(f)
    #         global fname
    #         for row in reader:
    #             fname = row[0].split()
    #             # print(row)
    #             # print(fname)
    #             _, created = cls.objects.update_or_create(
    #               dict = [
    #                 {'Full_Name': fname[0]+' '+fname[1],
    #                 'Lecturer_ID': row[1],
    #                 'Department': row[2],
    #                 'Category': row[3],
    #                 'Unit': row[4],
    #                 'Faculty': row[5],
    #                 'Date': row[6]
    #                 }
    #                 ]
    #             )
            #save the dict to the database
            # cls.objects.bulk_create(dict)
            # print(dict)

            
