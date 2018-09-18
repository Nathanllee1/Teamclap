from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser
'''
parent_student = [
    'parent',
    'student'
]

'''


class CustomUser(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    grade = models.PositiveIntegerField(default=9)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 #message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    phone = models.PositiveIntegerField(000-000-0000)

    #status = models.CharField(max_length=10, choices=parent_student, default='')
