from ..models import User
from ..serializers.user import UserShortSerializer, UserCreateSerializer

from rest_framework import viewsets

from ..permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserShortSerializer
    permission_classes = [UserPermission]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return super().get_serializer_class()
