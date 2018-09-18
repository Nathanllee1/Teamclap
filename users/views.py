from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser

#from .forms import CustomUserCreationForm


class SignUp(CreateView):
    model = CustomUser
    fields = ('name', 'email', 'phone')
    #form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
