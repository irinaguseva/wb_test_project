from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from ..models import Creator
from ..serializers import CreatorSerializer


class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

    @action(detail=True, methods=['post'])
    def transfer_money(self, request, pk=None):
        sender = self.get_object()
        receiver_id = request.data.get('receiver_id')
        amount = request.data.get('amount')

        if not receiver_id or not amount:
            return Response(
                {"error": "receiver_id and amount are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if sender.money < amount:
            return Response(
                {"error": "Not enough money"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            with transaction.atomic():
                receiver = Creator.objects.select_for_update().get(id=receiver_id)
                sender.money -= amount
                receiver.money += amount
                sender.save()
                receiver.save()
                sender.refresh_from_db()
                receiver.refresh_from_db()

        except Creator.DoesNotExist:
            return Response(
                {"error": "Receiver not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"status": f"Money transferred from {sender.name} ( {sender.money}$ left ) to {receiver.name} ( {receiver.money}$ left )"},
            status=status.HTTP_200_OK
        )