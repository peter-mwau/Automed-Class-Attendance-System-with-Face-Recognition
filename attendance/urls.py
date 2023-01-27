from django.urls import path
from . import views


# from xml.etree.ElementInclude import include


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('home/', views.home),
    path('capture/', views.reports),
    path('register/', views.register),
    # path('attendance/templates/attendance.csv', views.reports),
] 