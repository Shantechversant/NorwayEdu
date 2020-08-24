from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apis.serializers import UserSerializer
from users.models import CustomUser

class Users(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


