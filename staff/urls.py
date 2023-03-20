from django.conf import settings
from django.urls import path, include

from facedjango.settings import MEDIA_ROOT
from . import views
from django.conf import settings
from django.conf.urls import static
from attendance.views import index

# from xml.etree.ElementInclude import include
from .views import staff


urlpatterns = [
    path('', views.reports),
    # path('', views.staff)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)