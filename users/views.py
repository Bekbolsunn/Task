from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView

from users.models import User
from .serializers import (
    LoginSerializer, RegistrationSerializer
)


class RegistrationAPIView(CreateAPIView):
    
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    