from django.shortcuts import render
from django.views.generic import CreateView
from .form import *
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,LoginView
from django.utils.translation import activate
# Create your views here.

class SignUpView(CreateView): 
    form_class = SignUpForm 
    template_name = 'registration/signUp.html' 
    success_url = reverse_lazy('login')


class PasswordChange(PasswordChangeView):
    template_name = 'registration/password_change_form.html' 
    success_url = reverse_lazy('login')



