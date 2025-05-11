import httpx
from uuid import UUID, uuid4
from bot.dto.order import TotalOrderPrice
from bot.settings import Settings

API_URL = "https://api.yookassa.ru/v3/payments"
RETURN_URL = "https://t.me/"


class PaymentService:
    @staticmethod
    async def create_payment_link(
        user_id: UUID,
        product_id: UUID,
        quantity: int,
        total_price: float,
    ) -> tuple[str, UUID]:
        """Create payment link."""
        settings = Settings()

        idempotence_key = str(uuid4())

        # Формируем данные для запроса
        payment_data = {
            "amount": {
                "value": f"{total_price:.2f}",  # Общая сумма заказа
                "currency": "RUB",  # Валюта
            },
            "confirmation": {
                "type": "redirect",  # Тип подтверждения платежа
                "return_url": f"{RETURN_URL}{settings.bot.name}",  # URL для перенаправления после оплаты
            },
            "capture": True,  # Автоматическое подтверждение платежа
            "description": f"Заказ пользователя {user_id} на товар {product_id}",  # Описание платежа
            "metadata": {
                "user_id": str(user_id),  # ID пользователя для внутреннего использования
                "product_id": str(product_id),  # ID товара
                "quantity": quantity,  # Количество товара
            },
        }

        # Аутентификация через Basic Auth
        auth = (settings.yookassa.SHOP_ID, settings.yookassa.SECRET_KEY)

        # Отправляем POST-запрос к API YooKassa
        async with httpx.AsyncClient() as client:
            response = await client.post(
                API_URL,
                json=payment_data,
                auth=auth,
                headers={"Idempotence-Key": idempotence_key},  # Добавляем заголовок
            )

            # Проверяем успешность запроса
            if response.status_code == 200:
                payment_response = response.json()
                confirmation_url = payment_response["confirmation"]["confirmation_url"]
                payment_id = payment_response["id"]
                return confirmation_url, payment_id
            else:
                # Логируем ошибку и выбрасываем исключение
                error_message = f"Ошибка при создании ссылки на оплату: {response.text}"
                raise Exception(error_message)
