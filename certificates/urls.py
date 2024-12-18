from django.urls import path
from .views import *

urlpatterns = [
    path('newCertificateSettings/', NewCertificateSettings.as_view(), name='newCertificateSettings'),
]