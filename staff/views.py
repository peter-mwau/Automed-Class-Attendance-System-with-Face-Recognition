from django.shortcuts import render
from attendance.recognize import runFile
from .models import Lecturer_detail
from reports.views import read_csv

# Create your views here.

# def reports(request):
#     context = {}
#     runFile()
#     read_csv('attendance.csv')
#     return render(request, 'attendance.csv')


# def details(request):
#     lec_details = Lecturer_detail.objects.all()
#     now = datetime.now()
#     dtstring = now.strftime('%H:%M:%S')
#     f.writelines((f'\n{name},{dtstring}'))
#     return render(request, "Project.sqlite3", {'lec_details': lec_details})


