from django_filters import rest_framework as filters

from sprint.models import Sprint
from sprint.database_helpers import get_last_n_days_active_sprins


class SprintFilter(filters.FilterSet):
    start__gt = filters.DateTimeFilter(
        field_name='start_time', lookup_expr='gt'
    )
    start__lt = filters.DateTimeFilter(
        field_name='start_time', lookup_expr='lt'
    )
    last_n_days_active = filters.NumberFilter(method='get_last_n_days_active')

    class Meta:
        model = Sprint
        fields = [
            'start__gt',
            'start__lt',
            'team',
            'team__profiles',
            'last_n_days_active',
        ]

    def get_last_n_days_active(self, queryset, name, value):
        return queryset.filter(*get_last_n_days_active_sprins(value))
