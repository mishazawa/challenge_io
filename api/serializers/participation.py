from rest_framework import serializers

from ..models import Participation
from .user import UserShortSerializer


class ParticipantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = [
            "user",
            "challenge",
        ]

    def create(self, validated_data):
        return Participation.objects.get_or_create(**validated_data)


class ParticipationSerializer(serializers.HyperlinkedModelSerializer):
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
