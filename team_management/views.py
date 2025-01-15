from rest_framework import viewsets
from .models import Creator, Team, Member, TeamApplication
from .serializers import CreatorSerializer, TeamSerializer, MemberSerializer, TeamApplicationSerializer

class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class TeamApplicationViewSet(viewsets.ModelViewSet):
    queryset = TeamApplication.objects.all()
    serializer_class = TeamApplicationSerializer
