from django.db import models

from base.models import BaseMixin
from user.models import User
from task.models import Task
from sprint.models import Sprint

# Create your models here.


class UserHistory(BaseMixin):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    task = models.ForeignKey(
        Task,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    sprint = models.ForeignKey(
        Sprint,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )


class TaskStats(BaseMixin):
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    points = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = (('task', 'user'),)


class SprintStats(BaseMixin):
    sprint = models.ForeignKey(
        Sprint,
        on_delete=models.DO_NOTHING
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    total_points = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = (('sprint', 'user'), )
