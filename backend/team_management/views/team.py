from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Team, TeamApplication
from ..serializers import TeamSerializer


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