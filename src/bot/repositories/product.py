from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.models.inventory.products import Product
from bot.database.pg_database import SQLAlchemyDatabaseConnector
from bot.dto.product import CategoryDTO, ProductDTO


class ProductReader:
    sessionmaker = SQLAlchemyDatabaseConnector().get_master_session_maker()

    async def get_product_by_id(self, product_id: UUID) -> ProductDTO | None:
        stmt = select(Product).filter_by(id=product_id)
        stmt = stmt.filter(Product.is_deleted.isnot(True))
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if product_db := result.scalar():
                product = await self.get_product_dto(product_db)
                return product
        return None

    async def get_products(self, category_id: UUID | None = None) -> list[ProductDTO]:
        stmt = select(Product)
        if category_id:
            stmt = stmt.options(joinedload(Product.category))
            stmt = stmt.filter_by(category_id=category_id)
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if products := result.scalars():
                result_products = []
                for product_db in products:
                    product = await self.get_product_dto(product_db)
                    result_products.append(product)
                return result_products
            return []

    async def get_product_dto(self, product_db) -> ProductDTO:
        category = CategoryDTO(
            id=product_db.category.id,
            name=product_db.category.name,
        )
        product = ProductDTO(
            id=product_db.id,
            name=product_db.name,
            description=product_db.description,
            quantity=product_db.quantity,
            price=product_db.price,
            unit_of_measure=product_db.unit_of_measure,
            image_url=product_db.image_url,
            category=category,
        )
        return product
