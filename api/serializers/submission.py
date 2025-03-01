from rest_framework import serializers
from django.db import transaction

from ..models import Submission, Participation


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = [
            "created_at",
            "owner",
            "challenge",
            "description",
            "url",
        ]
        extra_kwargs = {"owner": {"read_only": True}, "challenge": {"read_only": True}}


class SubmissionCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = [
            "owner",
            "challenge",
            "description",
        ]
        extra_kwargs = {"owner": {"read_only": True}}

    def create(self, validated_data):
        with transaction.atomic():
            submission = Submission.objects.create(**validated_data)
            Participation.objects.get_or_create(
                user=validated_data.get("owner"),
                challenge=validated_data.get("challenge"),
            )
            return submission
