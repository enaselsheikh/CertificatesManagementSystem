from django.contrib import admin
from .models import CertificateSetting,CertificateType
# Register your models here.

admin.site.register(CertificateSetting)
admin.site.register(CertificateType)
