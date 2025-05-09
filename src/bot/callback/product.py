from uuid import UUID
from aiogram.filters.callback_data import CallbackData


class ProductCallbackData(CallbackData, prefix="product"):
    product_id: UUID


class DeliveryCallbackData(CallbackData, prefix="delivery"):
    pass
