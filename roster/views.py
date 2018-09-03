from django.shortcuts import render
from users import models

from django.views.generic import ListView
# Create your views here.
from users.models import CustomUser


class roster(ListView):
    model = CustomUser
    template_name = 'roster.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        return context
    #query_results = CustomUser.objects.all()

