from typing import List
from uuid import UUID
from bot.dto.product import CategoryDTO
from bot.repositories.category import CategoryReader


class CategoryService:
    @staticmethod
    async def get_categories(page: int, per_page: int) -> tuple[List[CategoryDTO], int]:
        # Здесь должна быть логика получения продуктов из базы данных
        # Пример: categories = await db.get_categories(page, per_page)
        Category_reader = CategoryReader()
        categories = await Category_reader.get_categories()
        total_pages = (len(categories) + per_page - 1) // per_page
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        return categories[start_index:end_index], total_pages

    @staticmethod
    async def get_category_by_id(category_id: UUID) -> CategoryDTO | None:
        # Здесь должна быть логика получения продукта по ID из базы данных
        # Пример: category = await db.get_category_by_id(category_id)
        Category_reader = CategoryReader()
        return await Category_reader.get_category_by_id(category_id)
