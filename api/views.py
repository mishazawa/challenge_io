from rest_framework import permissions, generics
from .serializers import UserShortSerializer, ChallengeSerializer, SubmissionSerializer, ParticipantsSerializer
from .models import Challenge, User, Submission, Participation
from rest_framework import serializers
from django.shortcuts import get_object_or_404

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserShortSerializer

class ChallengesListAPIView(generics.ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class ChallengesDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ChallengeSerializer

    def get_queryset(self):
        return Challenge.objects.filter(pk=self.kwargs["pk"])

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset)

class ParticipantsListAPIView(generics.ListAPIView):
    serializer_class = ParticipantsSerializer

    def get_queryset(self):
        return Participation.objects.filter(challenge=self.kwargs["pk"])
    

class SubmissionsListAPIView(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    
    def get_queryset(self):
        return Submission.objects.filter(challenge=self.kwargs["pk"])
    