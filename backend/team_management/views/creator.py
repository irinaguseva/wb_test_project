from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from ..models import Creator
from ..serializers import CreatorSerializer, TransferMoneySerializer
from drf_yasg.utils import swagger_auto_schema


class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

    @swagger_auto_schema(
        request_body=TransferMoneySerializer,
        responses={
            200: "Money transferred successfully",
            400: "Bad request (e.g., not enough money)",
            404: "Receiver not found",
            500: "Internal server error",
        },
        operation_description="Transfer money from one creator to another."
    )
    @action(detail=True, methods=['post'])
    def transfer_money(self, request, pk=None):
        """
        Передача денежных баллов от одного создателя другому.
        """
        # Получаем отправителя (sender)
        sender = self.get_object()

        # Валидируем тело запроса с помощью TransferMoneySerializer
        transfer_serializer = TransferMoneySerializer(data=request.data)
        transfer_serializer.is_valid(raise_exception=True)

        # Получаем данные из запроса
        receiver_id = transfer_serializer.validated_data['receiver_id']
        amount = transfer_serializer.validated_data['amount']

        # Проверяем, что у отправителя достаточно денег
        if sender.money < amount:
            return Response(
                {"error": "Not enough money"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Используем транзакцию для атомарности
            with transaction.atomic():
                # Блокируем запись получателя для избежания race condition
                receiver = Creator.objects.select_for_update().get(id=receiver_id)

                # Выполняем перевод
                sender.money -= amount
                receiver.money += amount

                # Сохраняем изменения
                sender.save()
                sender.refresh_from_db()
                receiver.save()
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

        # Возвращаем успешный ответ
        return Response(
            {"status": f"Money transferred from {sender.name} ( {sender.money}$ left ) to {receiver.name} ( {receiver.money}$ left )"},
            status=status.HTTP_200_OK
        )