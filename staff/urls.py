from django.conf import settings
from django.urls import path

from facedjango.settings import MEDIA_ROOT
from . import views
from django.conf import settings
from django.conf.urls import static
from attendance.views import index

from xml.etree.ElementInclude import include


urlpatterns = [
    # path('staff', views.index),
    path('', views.staff)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)