
from rest_framework import serializers

from .models import User, Challenge, Submission, Participation

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups'
        ]

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = [
            "created_at",
            "owner",
            "challenge",
            "description",
        ]

class ChallengeSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "start_date",
            "end_date",
            "owner",
            "participants",
        ]





