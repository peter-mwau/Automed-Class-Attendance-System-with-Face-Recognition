from .models import  Lecturer_report, Student_report
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string


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
def read_csv2(csv_name2):
    with open(csv_name2, 'r') as file:
        no_records = 0
        for row in file:
            print(row.split(',')[0])
            Student_report.objects.create(stud_names=row.split(',')[0], reg_no=row.split(',')[1], course=row.split(',')[2], cohort=row.split(',')[3], category=row.split(',')[4], unit=row.split(',')[5], dateofattendance=row.split(',')[6])
            no_records += 1
    print('\n{} Records inserted successfully'.format(no_records))



# a method to return a document as a downloadable file with reports from both the Student_report and Lecturer_report tables and return response to the dashboard in a pdf format.
def report(request):
    student = Student_report.objects.all()
    lecturer = Lecturer_report.objects.all()

    context = {
        'student': student,
        'lecturer': lecturer,
    }
    html = render_to_string('reports.html',context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Attendance Report.pdf"'
    pdf = pisa.CreatePDF(html, dest=response)
    if not pdf.err:
        return response
    return HttpResponse('Error generating PDF')

    # buffer = BytesIO()
    # p = canvas.Canvas(buffer)
    # # p = canvas.Canvas(response)
    # p.drawString(100, 100, html)
    # p.showPage()
    # p.save()
    # pdf = buffer.getvalue()
    # buffer.close()
    # response.write(pdf)
    # return response
# response['Content-Disposition'] = 'attachment; filename="Attendance Report.pdf"'
    
    


    





  
