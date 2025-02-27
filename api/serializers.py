
from rest_framework import serializers

from .models import User, Challenge, Submission, Participation

class UserShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
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

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    participants = serializers.HyperlinkedIdentityField(view_name='challenge-participants')
    submissions = serializers.HyperlinkedIdentityField(view_name='challenge-submissions')
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
            "url",
            "participants",
            "submissions",
        ]


class ParticipantsSerializer(serializers.HyperlinkedModelSerializer):
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = Participation
        fields = [
            "joined_at",
            "user",
        ]

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = rep.pop('user')
        for key in user:
            rep[key] = user[key]
        return rep