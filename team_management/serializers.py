from rest_framework import serializers
from .models import Creator, Team, Member, TeamApplication

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'

    #def validate_money(self, value):
        #if value < 0:
            #raise serializers.ValidationError("Money cannot be negative.")

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    #def validate_name(self, value):
        #if Team.objects.filter(name=value).exists():
            #raise serializers.ValidationError("Team with this name already exists.")
        #return value

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    #def validate_stamina(self, value):
        #if value < 0:
            #raise serializers.ValidationError("Stamina cannot be negative.")
        #return value

class TeamApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamApplication
        fields = '__all__'
