# Create your views here.
from django.views.generic.edit import CreateView
from .models import CertificateSetting
from .forms import NewCertificateSettingsForm

class NewCertificateSettings(CreateView):
    model = CertificateSetting
    form_class = NewCertificateSettingsForm
    template_name = 'certificates/new_certificate_settings.html'
    success_url = '/home/'
