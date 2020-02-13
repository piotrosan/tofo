from rest_framework import serializers

from stats.models import SprintStats, TaskStats, UserHistory
from sprint.models import Sprint
from task.models import Task
from team.models import Team
from userprofile.models import Profile
from machinelearning.models import UserCapabilities
from user.models import User


class ProfileSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=Profile.GENDER_CHOICES)

    class Meta:
        model = Profile
        fields = ('gender', 'team', 'age', 'pet')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = User.objects.create(validated_data, profile)
        return user

    def update(self, instance, validated_data):
        # profile = validated_data.pop('profile')
        user = User.objects.update(instance, validated_data)
        return user


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SprintSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.SlugRelatedField(
        queryset=Team.objects.all(),
        slug_field='name'
    )
    left_to_end = serializers.DurationField(read_only=True)

    class Meta:
        model = Sprint
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    worker = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    level = serializers.ChoiceField(choices=Task.LEVEL_CHOICES)
    urgent = serializers.ChoiceField(choices=Task.URGENT_CHOICES)
    sprint = serializers.SlugRelatedField(
        queryset=Sprint.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Task
        fields = '__all__'


class UserHistorySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    task = serializers.SlugRelatedField(
        queryset=Task.objects.all(),
        slug_field='name'
    )
    sprint = serializers.SlugRelatedField(
        queryset=Sprint.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = UserHistory
        fields = '__all__'


class SprintStatsSerializer(serializers.HyperlinkedModelSerializer):
    sprint = serializers.SlugRelatedField(
        queryset=Sprint.objects.all(),
        slug_field='name'
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = SprintStats
        fields = '__all__'


class TaskStatsSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.SlugRelatedField(
        queryset=Task.objects.all(),
        slug_field='name'
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = TaskStats
        fields = '__all__'


class UserCapabilitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCapabilities
        fields = '__all__'

