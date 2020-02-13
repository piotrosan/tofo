from collections import OrderedDict
from django.contrib.auth.models import User
from rest_framework import serializers

from machinelearning.tools import (
    predict_user_capabilites,
    compute_average_from_test,
)


class LearningCustomUserOrder(serializers.ChoiceField):

    def __init__(self, *agrs, **kwargs):
        self._choices = self.get_choices()
        super(LearningCustomUserOrder, self).__init__(*agrs, **kwargs)

    def get_choices(self):
        user_capabilites = predict_user_capabilites()
        return compute_average_from_test(user_capabilites)
