from django.db import models

from base.models import BaseMixin
from team.models import Team


class Profile(BaseMixin):
    # ToDo create enum from choices
    MALE = 'M'
    FEMALE = 'K'

    GENDER_CHOICES = (
        (MALE, 'Mężczyzna'),
        (FEMALE, 'Kobieta'),
    )
    team = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='profiles'
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )
    age = models.IntegerField(null=True, blank=True)
    pet = models.BooleanField(default=0)





