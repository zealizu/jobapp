# Generated by Django 5.0 on 2023-12-27 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_profilehr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateapplications',
            name='resume',
        ),
    ]
