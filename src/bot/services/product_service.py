# bot/services/product_service.py
from typing import List
from uuid import UUID
from bot.dto.product import ProductDTO
from bot.repositories.product import ProductReader


class ProductService:
    @staticmethod
    async def get_products(
        page: int,
        per_page: int,
        category_id: UUID | None = None,
    ) -> tuple[List[ProductDTO], int]:
        # Здесь должна быть логика получения продуктов из базы данных
        # Пример: products = await db.get_products(page, per_page)
        Product_reader = ProductReader()
        products = await Product_reader.get_products(category_id=category_id)
        total_pages = (len(products) + per_page - 1) // per_page
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        return products[start_index:end_index], total_pages

    @staticmethod
    async def get_product_by_id(product_id: UUID) -> ProductDTO | None:
        # Здесь должна быть логика получения продукта по ID из базы данных
        # Пример: product = await db.get_product_by_id(product_id)
        Product_reader = ProductReader()
        return await Product_reader.get_product_by_id(product_id)
