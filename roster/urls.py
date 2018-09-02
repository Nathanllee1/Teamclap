from django.urls import path

from .import views


urlpatterns = [
    path('roster/', views.roster.as_view(), name='roster'),
]