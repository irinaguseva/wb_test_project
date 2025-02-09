from rest_framework import serializers
from .models import Creator, Team, Member, TeamApplication


class TransferMoneySerializer(serializers.Serializer):
    receiver_id = serializers.IntegerField(required=True)
    amount = serializers.FloatField(required=True, min_value=0)


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

    def create(self, validated_data):
        """
        Создание нового создателя.
        """
        return Creator.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновление существующего создателя.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.money = validated_data.get('money', instance.money)
        instance.save()
        return instance


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'creator']

    def validate_name(self, value):
        """
        Проверка уникальности названия команды.
        """
        if Team.objects.filter(name=value).exists():
            raise serializers.ValidationError("Team with this name already exists.")
        return value

    def create(self, validated_data):
        """
        Создание новой команды.
        """
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновление существующей команды.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.save()
        return instance


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

    def create(self, validated_data):
        """
        Создание нового участника.
        """
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновление существующего участника.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.endurance = validated_data.get('endurance', instance.endurance)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance


class TeamApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamApplication
        fields = ['id', 'member', 'team']

    def create(self, validated_data):
        """
        Создание новой заявки.
        """
        return TeamApplication.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновление существующей заявки.
        """
        instance.member = validated_data.get('member', instance.member)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance