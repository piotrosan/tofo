import datetime
import pytz

from django.db.models import Q


def get_last_n_days_active_sprins(value):
    return [
        Q(start_time__lte=datetime.datetime.now(pytz.utc)),
        Q(end_time__gte=datetime.datetime.now(pytz.utc)),
        Q(start_time__gte=
            datetime.datetime.now(pytz.utc) -
            datetime.timedelta(days=int(value))
        ),
    ]
