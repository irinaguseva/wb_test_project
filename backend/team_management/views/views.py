from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Creator, Team, Member, TeamApplication
from ..serializers import CreatorSerializer, TeamSerializer, MemberSerializer, TeamApplicationSerializer


class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

    @action(detail=True, methods=['post'])
    def transfer_money(self, request, pk=None):
        sender = self.get_object()
        receiver_id = request.data.get('receiver_id')
        amount = request.data.get('amount')

        if sender.money < amount:
            return Response({"error": "Not enough money"}, status=status.HTTP_400_BAD_REQUEST)

        receiver = Creator.objects.get(id=receiver_id)
        sender.money -= amount
        receiver.money += amount
        sender.save()
        receiver.save()

        return Response({"status": "Money transferred"}, status=status.HTTP_200_OK)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=['post'])
    def process_applications(self, request, pk=None):
        team = self.get_object()
        applications = TeamApplication.objects.filter(team=team).order_by('-member__endurance')[:10]

        for application in applications:
            team.member_set.add(application.member)
            application.delete()

        return Response({"status": "Applications processed"}, status=status.HTTP_200_OK)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class TeamApplicationViewSet(viewsets.ModelViewSet):
    queryset = TeamApplication.objects.all()
    serializer_class = TeamApplicationSerializer