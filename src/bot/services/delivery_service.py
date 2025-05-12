from bot.dto.order import TotalOrderPrice


class DeliveryService:

    @staticmethod
    async def calculate_delivery_cost(price: float, quantity: int, address: str) -> TotalOrderPrice:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        
        product_price = float(price * quantity)
        delivery_price = float(2500)
        vat_price = float(product_price * 0.2)
        total_price = product_price + delivery_price + vat_price
        return TotalOrderPrice(
            product_price=product_price,
            delivery_price=delivery_price,
            vat_price=vat_price,
            total_price=total_price,
        )
