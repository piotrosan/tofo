from django.db import models

from base.models import BaseMixin


class Team(BaseMixin):
    name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.name
