"""kivy_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from auth.viewsets import LoginWithToken
from webapi import viewsets
from userprofile.views import ProfileSite
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djose/auth/', include('djoser.urls.authtoken')),
    # implement django rest built-in function
    path('rest/auth/', LoginWithToken.as_view()),
    path('jwt/auth/', obtain_jwt_token),
    path(
        r'sprints/',
        viewsets.SprintList.as_view(),
        name=viewsets.SprintList.name),
    path(
        r'sprint/<int:pk>/',
        viewsets.SprintDetail.as_view(),
        name=viewsets.SprintDetail.name),
    path(
        r'tasks/',
        viewsets.TaskList.as_view(),
        name=viewsets.TaskList.name),
    path(
        r'task/<int:pk>/',
        viewsets.TaskDetail.as_view(),
        name=viewsets.TaskDetail.name),
    path(
        r'teams/',
        viewsets.TeamList.as_view(),
        name=viewsets.TeamList.name),
    path(
        r'team/<int:pk>/',
        viewsets.TeamDetail.as_view(),
        name=viewsets.TeamDetail.name),
    path(
        r'users/',
        viewsets.UserList.as_view(),
        name=viewsets.UserList.name),
    path(
        r'user/<int:pk>/',
        viewsets.UserDetail.as_view(),
        name=viewsets.UserDetail.name),
    path(
        r'usersprofile/',
        viewsets.UserProfileList.as_view(),
        name=viewsets.UserProfileList.name),
    path(
        r'userprofile/<int:pk>/',
        viewsets.UserProfileDetail.as_view(),
        name=viewsets.UserProfileDetail.name),
    path(
        r'usershistory/',
        viewsets.UserHistoryList.as_view(),
        name=viewsets.UserHistoryList.name),
    path(
        r'spritnstats/',
        viewsets.SprintStatsList.as_view(),
        name=viewsets.SprintStatsList.name),
    path(
        r'taskstats/',
        viewsets.TaskStatsList.as_view(),
        name=viewsets.TaskStatsList.name),
    path(
        r'users/me/',
        viewsets.ProfileSite.as_view(),
        name=ProfileSite.name),
    path(
        r'usercapabilites/',
        viewsets.UserCapabilitiesList.as_view(),
        name=viewsets.UserCapabilitiesList.name),
    path(
        r'hint/',
        viewsets.HintList.as_view({'get': 'list'}),
        name=viewsets.HintList.name),
    path(
        r'newusers/',
        viewsets.NewUserViewSet.as_view({
            'get': 'list',
            'post': 'create'}),
        name=viewsets.NewUserViewSet.name),
    path(
        r'newuser/<int:pk>/',
        viewsets.NewUserRetriveUpdateViewSet.as_view({
            'get': 'retrieve',
            'put': 'update'}),
        name=viewsets.NewUserRetriveUpdateViewSet.name),

]