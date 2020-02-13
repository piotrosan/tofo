import datetime
import pytz

from django.db import models

from base.models import BaseMixin
from team.models import Team


class Sprint(BaseMixin):
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    team = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    real_end_time = models.DateTimeField(null=True, blank=True)

    @property
    def left_to_end(self):
        if all([self.end_time]):
            return self.end_time - datetime.datetime.now(pytz.utc)
        return datetime.timedelta(days=0)



