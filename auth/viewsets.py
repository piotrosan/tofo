
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from auth.serializers import LoginSerializer
from auth.tools import login_with_token


class LoginWithToken(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = login_with_token(request, serializer.user)
            return Response({
                'token': token.key,
            })

        return Response(serializer.errors)
