# Generated by Django 2.1.2 on 2018-12-30 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20181230_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]