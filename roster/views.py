from django.shortcuts import render
from users import models

from django.views.generic import ListView
# Create your views here.

class roster(ListView):
    template_name = 'roster.html'
    model = models.CustomUser