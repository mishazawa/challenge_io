from rest_framework import permissions, generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    UserShortSerializer,
    ParticipationsSerializer,
    ChallengeSerializer,
    SubmissionSerializer,
    ParticipantsSerializer,
)
from .models import Challenge, User, Submission, Participation


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserShortSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
