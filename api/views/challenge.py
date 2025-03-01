from ..models import Challenge, Submission, Participation
from ..permissions import IsOwnerOrAdmin
from ..serializers.participation import (
    ParticipationSerializer,
    ParticipantsSerializer,
    ParticipantCreateSerializer,
)
from ..serializers.submission import (
    SubmissionSerializer,
)
from ..serializers.challenge import (
    ChallengeSerializer,
    ChallengeCreateSerializer,
)

from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import transaction


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

    # TODO: maybe split to separate view for participations
    @action(
        detail=False, permission_classes=[permissions.IsAuthenticated], url_path="my"
    )
    def my_participations(self, request):
        participants = Participation.objects.filter(user=self.request.user)
        serializer = ParticipationSerializer(
            participants, many=True, context={"request": request}
        )
        return Response(serializer.data)

    # TODO: maybe split to separate view for participations
    @action(
        detail=True,
        methods=["get", "post", "delete"],
        permission_classes=[permissions.IsAuthenticated],
        url_path=r"participants",
        url_name="participants",
    )
    def get_participants(self, request, pk=None):
        if request.method == "POST":
            serializer = ParticipantCreateSerializer(
                data={
                    "challenge": pk,
                    "user": self.request.user.id,
                },
                context={"request": request},
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            with transaction.atomic():
                participants = Participation.objects.filter(
                    challenge=pk, user=self.request.user.id
                )

                for p in participants:
                    p.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)

        # GET list of participant to the current challenge
        participants = Participation.objects.filter(challenge=pk)
        serializer = ParticipantsSerializer(
            participants, many=True, context={"request": request}
        )
        self.paginate_queryset(participants)
        return self.get_paginated_response(serializer.data)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[permissions.IsAuthenticated],
        url_path=r"submissions",
        url_name="submissions",
    )
    def get_submissions(self, request, pk=None):
        # GET list of submissions to the current challenge
        submissions = Submission.objects.filter(challenge=pk)
        serializer = SubmissionSerializer(
            submissions, many=True, context={"request": request}
        )
        self.paginate_queryset(submissions)
        return self.get_paginated_response(serializer.data)
