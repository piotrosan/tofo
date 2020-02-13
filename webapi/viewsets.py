from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from stats.models import SprintStats, TaskStats, UserHistory
from sprint.models import Sprint
from userprofile.models import Profile
from sprint.filters import SprintFilter
from task.models import Task
from team.models import Team
from user.models import User

from machinelearning.models import UserCapabilities
from machinelearning.tools import (
    predict_user_capabilites,
    compute_average_from_test,
)

from webapi.serializers import (
    SprintSerializer,
    TaskSerializer,
    TeamSerializer,
    ProfileSerializer,
    UserSerializer,
    UserHistorySerializer,
    SprintStatsSerializer,
    TaskStatsSerializer,
    UserCapabilitiesSerializer,
)


class SprintList(generics.ListCreateAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    name = 'sprint-list'
    search_fields = ('team__name', 'team__profiles__user__username')
    filterset_class = SprintFilter
    # filter_backends = (filters.DjangoFilterBackend,)


class SprintDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    name = 'sprint-detail'


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-list'
    filter_fields = ('worker', )
    search_fields = ('worker__username', )


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-detail'


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-list'


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-detail'


class UserProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny, )
    name = 'user-profile-list'


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)
    name = 'user-profile-detail'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    name = 'user-detail'


class UserHistoryList(generics.ListCreateAPIView):
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer
    name = 'user-history-list'


class SprintStatsList(generics.ListCreateAPIView):
    queryset = SprintStats.objects.all()
    serializer_class = SprintStatsSerializer
    name = 'sprint-stats-list'


class TaskStatsList(generics.ListCreateAPIView):
    queryset = TaskStats.objects.all()
    serializer_class = TaskStatsSerializer
    name = 'task-stats-list'


class ProfileSite(generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'user-profile-site'

    def get(self, request):
        userprofile = get_object_or_404(
            self.get_queryset(), user=self.request.user
        )
        serializer = ProfileSerializer(userprofile)
        return Response(serializer.data)


class UserCapabilitiesList(generics.ListCreateAPIView):
    queryset = UserCapabilities.objects.all()
    serializer_class = UserCapabilitiesSerializer
    name = 'user-capability-list'


class HintList(viewsets.ViewSet):
    name = 'hint-list'

    def list(self, request):
        user_capabilites = predict_user_capabilites()
        result = ';'.join(
            [user[1] for user in compute_average_from_test(user_capabilites)])
        return Response(result)


class NewUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    name = 'new-user-view'


class NewUserRetriveUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    name = 'new-user-view'
