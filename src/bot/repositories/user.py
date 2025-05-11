from uuid import UUID
from sqlalchemy import select, insert, update
from sqlalchemy.orm import joinedload

from app.models.customer.customers import Customer
from bot.database.pg_database import SQLAlchemyDatabaseConnector
from bot.dto.user import UserCreateDTO, UserDTO, UserUpdateDTO


class UserRepository:
    sessionmaker = SQLAlchemyDatabaseConnector().get_master_session_maker()

    async def get_user_by_id(self, user_id: UUID) -> UserDTO | None:
        stmt = select(Customer).filter_by(id=user_id)
        stmt = stmt.filter(Customer.is_deleted.isnot(True))
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if user_db := result.scalar():
                user = await self.get_user_dto(user_db)
                return user
        return None

    async def get_user_by_telegram_id(self, telegram_user_id: int) -> UserDTO | None:
        stmt = select(Customer).filter_by(telegram_user_id=telegram_user_id)
        stmt = stmt.filter(Customer.is_deleted.isnot(True))
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if user_db := result.scalar():
                user = await self.get_user_dto(user_db)
                return user
        return None

    async def create_user(self, user_create_dto: UserCreateDTO) -> UserDTO | None:
        stmt = insert(Customer)
        stmt = stmt.values(user_create_dto.as_dict()).returning(Customer)
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if user_db := result.scalar():
                user = await self.get_user_dto(user_db)
            await session.commit()
            return user

    async def update_user(self, user_update_dto: UserUpdateDTO) -> UserDTO | None:
        data = {
            "phone_number": user_update_dto.phone_number,
        }
        stmt = update(Customer).filter_by(id=user_update_dto.user_id)
        stmt = stmt.values(data).returning(Customer)
        async with self.sessionmaker() as session:
            result = await session.execute(stmt)
            if user_db := result.scalar():
                user = await self.get_user_dto(user_db)
            await session.commit()
            return user

    async def get_user_dto(self, user_db) -> UserDTO:
        user = UserDTO(
            id=user_db.id,
            telegram_user_id=user_db.telegram_user_id,
        )
        return user
