from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.adduser, name='adduser')
]
