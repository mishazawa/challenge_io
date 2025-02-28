from ..models import User
from ..serializers import (
    UserShortSerializer,
)

from rest_framework import permissions, generics


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserShortSerializer
    permission_classes = [permissions.IsAuthenticated]
