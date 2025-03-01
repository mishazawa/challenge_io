from ..models import User
from ..serializers.user import (
    UserShortSerializer,
)

from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserShortSerializer
    permission_classes = [permissions.IsAuthenticated]
