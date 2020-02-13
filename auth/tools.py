from django.contrib.auth import login
from rest_framework.authtoken.models import Token


def login_with_token(request, user, with_session=True):
    token, created = Token.objects.get_or_create(user=user)
    if with_session:
        login(request, user)
    return token
