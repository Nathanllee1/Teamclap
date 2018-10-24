from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from .forms import AddForm

from django.core.mail import send_mail
from users.models import CustomUser


from django.urls import reverse_lazy


def adduser(request):
    template_name = 'teammanagement.html'
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # post dependent
            '''
            invite = Invitation.create('email@example.com', inviter=request.user)
            invite.send_invitation(request)
            '''

    else:
        form = AddForm

    return render(request, template_name, {'form': form})

