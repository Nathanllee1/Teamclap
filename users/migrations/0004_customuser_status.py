# Generated by Django 2.1.2 on 2018-10-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180817_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(default='Athlete', max_length=20),
        ),
    ]