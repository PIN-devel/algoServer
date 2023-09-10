from rest_framework import serializers

from problems.serializers import ProblemSerializer
from users.serializers import UserSerializer
from .models import Group, Round


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'


class RoundDetailSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    problems = ProblemSerializer(many=True)

    class Meta:
        model = Round
        fields = '__all__'
