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

    @classmethod
    def getLecturer(cls,first,second):
        results = cls.objects.get(fname = first, lname = second)
        return results



#  A function to create a table in database and commit data from csv file to database with the specified columns
    @classmethod
    def create_table(cls, csv_name):
        import csv
        from attendance import recognize
        csv_name = 'attendance.csv'
        with open(csv_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # print(row)
                _, created = cls.objects.update_or_create(
                    Full_Name=row[0],
                    Lecturer_ID=row[1],
                    Department=row[2],
                    Unit=row[3],
                    Faculty=row[4],
                    Date=row[5],
                )
