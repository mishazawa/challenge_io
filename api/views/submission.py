from ..models import Submission
from ..permissions import IsOwnerOrAdmin
from ..serializers.submission import (
    SubmissionSerializer,
    SubmissionCreateSerializer,
)

from rest_framework import permissions, viewsets


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return SubmissionCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]

        return [permission() for permission in self.permission_classes]

    def list(self, request):
        qs = self.get_queryset().filter(owner=request.user)
        serializer = SubmissionSerializer(qs, many=True, context={"request": request})
        self.paginate_queryset(qs)
        return self.get_paginated_response(serializer.data)
