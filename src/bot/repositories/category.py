from uuid import UUID
from sqlalchemy import select

from app.models.inventory.categories import Category
from bot.database.pg_database import SQLAlchemyDatabaseConnector
from bot.dto.product import CategoryDTO


class CategoryReader:
    sessionmaker = SQLAlchemyDatabaseConnector().get_master_session_maker()

    async def get_category_by_id(self, category_id: UUID) -> CategoryDTO | None:
        stmt = select(Category).filter_by(id=category_id)
        stmt = stmt.filter(Category.is_deleted.isnot(True))
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if category_db := result.scalar():
                category = CategoryDTO(
                    id=category_db.id,
                    name=category_db.name,
                )
                return category
        return None

    async def get_categories(self) -> list[CategoryDTO]:
        stmt = select(Category).order_by(Category.name)
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if categories := result.scalars():
                result_categories = []
                for category_db in categories:
                    category = CategoryDTO(
                        id=category_db.id,
                        name=category_db.name,
                    )
                    result_categories.append(category)
                return result_categories
            return []
