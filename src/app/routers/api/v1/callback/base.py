from fastapi import APIRouter, HTTPException, Request, status as http_status
import logging

from app.dependencies import OrderServiceDep
from app.dto.order.base import OrderUpdateDTO
from app.schemas.response.base import ResponseSchema
from app.settings import Settings  # Предполагается, что здесь хранятся настройки, включая секретный ключ YooKassa

router = APIRouter(prefix="/callback", tags=["Callbacks"])

logger = logging.getLogger(__name__)
settings = Settings()


@router.post(
    '/',
    summary="Обработка callback от YooKassa",
    status_code=http_status.HTTP_200_OK,
    response_model=ResponseSchema,
)
async def handle_yookassa_callback(
    request: Request,
    order_service: OrderServiceDep,
):
    """
    Обрабатывает callback-уведомления от YooKassa.
    """
    try:
        data = await request.json()
        logger.warning(f"Получен callback от YooKassa: {data}")

        event_type = data.get("event")  # Тип события (например, "payment.succeeded")
        payment_data = data.get("object")  # Данные платежа

        if event_type == "payment.succeeded":
            payment_id = payment_data.get("id")
            status = payment_data.get("status")
            await order_service.update_order(OrderUpdateDTO(payment_id=payment_id, status=status, success=True))
            logger.info(f"Платеж {payment_id} успешно обработан. Статус: {status}")

        elif event_type == "payment.canceled":
            payment_id = payment_data.get("id")
            status = payment_data.get("status")
            await order_service.update_order(OrderUpdateDTO(payment_id=payment_id, status=status, success=False))
            logger.info(f"Платеж {payment_id} отменен. Статус: {status}")
        else:
            logger.warning(f"Неизвестный тип события: {event_type}")
            return ResponseSchema(success=0)

        return ResponseSchema(success=1)

    except Exception as e:
        logger.error(f"Ошибка при обработке callback-а: {str(e)}")
        raise HTTPException(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка сервера")
