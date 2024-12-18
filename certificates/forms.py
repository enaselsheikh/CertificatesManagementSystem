from django import forms
from .models import CertificateSetting

class NewCertificateSettingsForm(forms.ModelForm):
    class Meta: 
        model = CertificateSetting 
        fields = ['name','image_location', 'certificate_content']