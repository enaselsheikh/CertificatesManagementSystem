from django.db import models

# Create your models here.


class CertificateType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    desc = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


class CertificateSetting(models.Model):
    imageLocationCoices = [(1,'اعلي اليمين'),(2,'اعلي اليسار')]
    name = models.CharField(max_length=50,null=False,blank=False)
    has_image = models.BooleanField(null=False)
    image_location = models.CharField(max_length=25, choices=imageLocationCoices, default=1)
    certificate_content = models.TextField(null=False,blank=False)
    CertificateType = models.ForeignKey(CertificateType,related_name='CertificateType',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

