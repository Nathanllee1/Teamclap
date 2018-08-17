from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect


from django.core.mail import send_mail
from users.models import CustomUser
from .forms import EmailForm

#class HomePageView(TemplateView):

    #template_name = 'sendEmail.html'


def emailSend(request):
    template_name = 'sendEmail.html'
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # post dependent
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # database dependent
            recipients = CustomUser.objects.all().values_list('email', flat=True)
            useremail = request.user.email

            send_mail(subject, message, useremail, recipients)

    else:
        form = EmailForm

    return render(request, template_name, {'form': form})
