from rest_framework import serializers
from .models import Creator, Team, Member, TeamApplication


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ['id', 'name', 'money']

    def validate_money(self, value):
        """
        Проверка, что money не отрицательное.
        """
        if value < 0:
            raise serializers.ValidationError("Money cannot be negative.")
        return value

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'creator']

    # Уникальность name уже проверяется на уровне модели (unique=True),
    # поэтому дополнительный валидатор не нужен.

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'endurance', 'team']

    def validate_endurance(self, value):
        """
        Проверка, что endurance не отрицательное.
        """
        if value < 0:
            raise serializers.ValidationError("Endurance cannot be negative.")
        return value

class TeamApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamApplication
        fields = ['id', 'member', 'team']