from django.shortcuts import render

# Create your views here.

def sync(request):
    template_name = 'sync.html'

    return render(request, template_name)