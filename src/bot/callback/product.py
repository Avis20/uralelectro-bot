from uuid import UUID
from aiogram.filters.callback_data import CallbackData


class ProductCallbackData(CallbackData, prefix="product"):
    """
    Callback data for product
    """

    product_id: UUID
