from rest_framework import serializers
from .models import Creator, Team, Member, TeamApplication

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class TeamApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamApplication
        fields = '__all__'
