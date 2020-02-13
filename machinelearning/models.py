from django.db import models

# Create your models here.


class UserCapabilities(models.Model):
    user = models.CharField(max_length=255)
    task_level = models.IntegerField()
    task_helpers = models.BooleanField()
    task_points = models.BooleanField()
