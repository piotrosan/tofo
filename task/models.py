from django.db import models

from user.models import User
from base.models import BaseMixin

from sprint.models import Sprint


class Task(BaseMixin):
    BASIC = 0
    NORMAL = 1
    MEDIUM = 2
    INTERMEDIATE = 3
    ADVANCED = 4

    LEVEL_CHOICES = (
        (BASIC, 'Podstawowy'),
        (NORMAL, 'Normalny'),
        (MEDIUM, 'Średni'),
        (INTERMEDIATE, 'Średniozaawansowany'),
        (ADVANCED, 'Zaawansowany'),
    )

    VERY_SLOW = 0
    SLOW = 1
    NORMAL = 2
    FAST = 3
    VERY_FAST = 4

    URGENT_CHOICES = (
        (VERY_SLOW, 'Bardzo Wolny'),
        (SLOW, 'Wolny'),
        (NORMAL, 'Normalny'),
        (FAST, 'Szybki'),
        (VERY_FAST, 'Bardzo Szybki'),
    )

    name = models.CharField(max_length=254)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    urgent = models.IntegerField(choices=URGENT_CHOICES)
    worker = models.ForeignKey(
        User,
        null=True,
        blank=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name='worker_task'
    )
    helpers = models.ManyToManyField(User)
    description = models.TextField()
    points = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    sprint = models.ForeignKey(
        Sprint,
        null=True,
        blank=True,
        related_name='tasks',
        on_delete=models.SET_NULL
    )
