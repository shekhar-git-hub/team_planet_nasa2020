# Generated by Django 3.1.2 on 2020-10-04 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]