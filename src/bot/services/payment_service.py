from uuid import UUID
from bot.dto.order import TotalOrderPrice


class PaymentService:

    @staticmethod
    async def create_payment_link(
        user_id: UUID,
        product_id: UUID,
        quantity: int,
        total_price: TotalOrderPrice,
    ) -> str:
        """Create payment link."""
        return "https://yoomoney.ru/"
