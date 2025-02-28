import datetime
from rest_framework import serializers
from .models import User, Challenge, Submission, Participation


class UserShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "username",
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


class ChallengeCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name="user-detail")

    start_date = serializers.DateField(initial=datetime.date.today)
    end_date = serializers.DateField(
        initial=datetime.date.today() + datetime.timedelta(days=7)
    )

    class Meta:
        model = Challenge
        fields = [
            "url",
            "title",
            "description",
            "start_date",
            "end_date",
            "owner",
        ]

    def create(self, validated_data):
        challenge = Challenge.objects.create(**validated_data)
        Participation.objects.create(
            user=validated_data.get("owner"), challenge=challenge
        )

        return challenge


class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    participants = serializers.HyperlinkedIdentityField(
        view_name="challenge-participants"
    )
    submissions = serializers.HyperlinkedIdentityField(
        view_name="challenge-submissions"
    )

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
        extra_kwargs = {"owner": {"read_only": True}}


class ParticipationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participation
        fields = [
            "joined_at",
            "challenge",
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
        user = rep.pop("user")
        for key in user:
            rep[key] = user[key]
        return rep
