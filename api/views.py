from rest_framework import permissions, viewsets, generics
from .serializers import UserSerializer, ChallengeSerializer, SubmissionSerializer
from .models import Challenge, User, Submission

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChallengeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows challenges to be viewed or edited.
    """
    
    queryset = Challenge.objects.all().order_by('-created_at')
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows submissions to be viewed or edited.
    """
    
    queryset = Submission.objects.all().order_by('-created_at')
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
