from uuid import UUID
from sqlalchemy import select, insert

from app.models.order.orders import Order
from app.models.order.status import OrderStatus
from bot.database.pg_database import SQLAlchemyDatabaseConnector
from bot.dto.order import OrderCreateDTO, OrderDTO


class OrderRepository:
    sessionmaker = SQLAlchemyDatabaseConnector().get_master_session_maker()

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
        order = OrderDTO(
            id=order_db.id,
            customer_id=order_db.customer_id,
            product_id=order_db.product_id,
            order_date=order_db.order_date,
            order_status_id=order_db.order_status_id,
            employee_id=order_db.employee_id,
            actual_delivery_date=order_db.actual_delivery_date,
        )
        return order
