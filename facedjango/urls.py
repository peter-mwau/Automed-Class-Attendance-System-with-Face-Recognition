from django.contrib import admin
from django.urls import path,include

import attendance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('attendance.urls')),
    # path('', include('attendance.urls')),
    path('', include('reports.urls')),
    path('', include('django.contrib.auth.urls')),
]
#    path('templates/', include('attendance.urls')),
#
#