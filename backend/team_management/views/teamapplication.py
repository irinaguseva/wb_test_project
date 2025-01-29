from rest_framework import viewsets
from ..models import TeamApplication
from ..serializers import TeamApplicationSerializer


class TeamApplicationViewSet(viewsets.ModelViewSet):
    queryset = TeamApplication.objects.all()
    serializer_class = TeamApplicationSerializer