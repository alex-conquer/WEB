# Generated by Django 5.0.3 on 2024-04-08 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
