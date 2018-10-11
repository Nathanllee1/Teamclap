from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
'''
parent_student = [
    'parent',
    'student'
]

'''

class CustomUser(AbstractUser):
    grade = models.PositiveIntegerField(default=9)
    phone = models.PositiveIntegerField(000-000-0000)
    status = models.CharField(max_length=20, default='Athlete')
    #status = models.CharField(max_length=10, choices=parent_student, default='')
