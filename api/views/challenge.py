from ..models import Challenge, Submission, Participation
from ..permissions import IsOwnerOrAdmin
from ..serializers import (
    ParticipationsSerializer,
    ChallengeSerializer,
    SubmissionSerializer,
    ParticipantsSerializer,
    ChallengeCreateSerializer,
)

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return ChallengeCreateSerializer
        return super().get_serializer_class()

    @action(
        detail=False, permission_classes=[permissions.IsAuthenticated], url_path="my"
    )
    def my_participations(self, request):
        participants = Participation.objects.filter(user=self.request.user)
        serializer = ParticipationsSerializer(
            participants, many=True, context={"request": request}
        )
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[permissions.IsAuthenticated],
        url_path=r"(?P<pk>\d+)/participants",
        url_name="participants",
    )
    def get_participants(self, request, pk=None):
        participants = Participation.objects.filter(challenge=pk)
        serializer = ParticipantsSerializer(
            participants, many=True, context={"request": request}
        )
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[permissions.IsAuthenticated],
        url_path=r"(?P<pk>\d+)/submissions",
        url_name="submissions",
    )
    def get_submissions(self, request, pk=None):
        s = Submission.objects.filter(challenge=pk)
        serializer = SubmissionSerializer(s, many=True, context={"request": request})
        return Response(serializer.data)
