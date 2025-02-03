from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from ..models import Team, TeamApplication
from ..serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=['post'])
    def process_applications(self, request, pk=None):
        team = self.get_object()
        try:
            with transaction.atomic():
                applications = TeamApplication.objects.filter(team=team).order_by('-member__endurance')[:10]

                for application in applications:
                    team.member_set.add(application.member)
                    application.delete()

                return Response({"status": "Applications processed"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)