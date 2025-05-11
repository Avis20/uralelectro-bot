from uuid import UUID
from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from app.models.inventory.products import Product
from app.models.order.orders import Order
from app.models.order.status import OrderStatus
from bot.database.pg_database import SQLAlchemyDatabaseConnector
from bot.dto.order import OrderCreateDTO, OrderDTO, OrderStatusDTO
from bot.dto.product import ProductDTO


class OrderRepository:
    sessionmaker = SQLAlchemyDatabaseConnector().get_master_session_maker()

    async def get_order_list(self, user_id: UUID) -> list[OrderDTO] | None:
        stmt = select(Order).filter_by(customer_id=user_id)
        stmt = stmt.options(joinedload(Order.product))
        stmt = stmt.options(joinedload(Order.order_status))
        stmt = stmt.filter(Order.is_deleted.isnot(True))
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if order_db_list := result.scalars().all():
                return [await self.get_order_dto(order_db) for order_db in order_db_list]
        return None

    async def get_order_new_status_id(self) -> UUID | None:
        stmt = select(OrderStatus).filter_by(name="Новый")
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if order_status_db := result.scalar():
                return order_status_db.id
        return None

    async def get_order_by_id(self, order_id: UUID) -> OrderDTO | None:
        stmt = select(Order).filter_by(id=order_id)
        stmt = stmt.filter(Order.is_deleted.isnot(True))
        stmt = stmt.options(joinedload(Order.order_status))
        stmt = stmt.options(joinedload(Order.product))
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if order_db := result.scalar():
                order = await self.get_order_dto(order_db)
                return order
        return None

    async def create_order(self, order_create_dto: OrderCreateDTO) -> OrderDTO | None:
        stmt = insert(Order)
        stmt = stmt.values(order_create_dto.as_dict()).returning(Order)
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if order_db := result.scalar():
                order = await self.get_order_dto(order_db)
            await session.commit()
            return order

    async def get_order_dto(self, order_db) -> OrderDTO:
        product = ProductDTO(
            id=order_db.product.id,
            name=order_db.product.name,
            description=order_db.product.description,
            price=order_db.product.price,
            unit_of_measure=order_db.product.unit_of_measure,
            image_url=order_db.product.image_url,
        )
        status = OrderStatusDTO(
            id=order_db.order_status.id,
            name=order_db.order_status.name,
        )
        order = OrderDTO(
            id=order_db.id,
            order_number=order_db.order_number,
            quantity=order_db.quantity,
            address=order_db.address,
            comment=order_db.comment,
            customer_id=order_db.customer_id,
            product_id=order_db.product_id,
            order_date=order_db.order_date,
            order_status_id=order_db.order_status_id,
            employee_id=order_db.employee_id,
            actual_delivery_date=order_db.actual_delivery_date,
            product=product,
            order_status=status,
        )
        return order
