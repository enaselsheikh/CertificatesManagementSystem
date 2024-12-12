from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]