# Generated by Django 3.2.9 on 2021-11-03 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]