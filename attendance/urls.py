from django.urls import path
from . import views
# import url 
from django.urls import re_path


# from xml.etree.ElementInclude import include


urlpatterns = [
    path('', views.login_user),
    path('login_user', views.login_user, name='login_user'),
    path('dashboard/', views.home, name='home'),
    path('capture/', views.reports,name='reports'),
    path('logout_user/', views.logout_user, name='logout_user'),
    # re_path(r'^capture/(?P<camera>\d+)/$', views.reports, name='reports'),
    path('register_user/', views.register_user, name='register_user'),
    path('dashboard/capture/', views.capture, name='capture'),
    path('capture/', views.reports, name='take_attendance'),
    # path('graph/', views.graph, name='graph'),
] 