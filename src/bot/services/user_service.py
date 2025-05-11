from typing import List
from uuid import UUID
from bot.dto.user import UserCreateDTO, UserDTO, UserUpdateDTO
from bot.repositories.user import UserRepository


class UserService:

    @staticmethod
    async def create_user(user_create_dto: UserCreateDTO) -> UserDTO | None:
        user_reader = UserRepository()
        return await user_reader.create_user(user_create_dto)

    @staticmethod
    async def update_user(user_update_dto: UserUpdateDTO) -> UserDTO | None:
        user_repo = UserRepository()
        return await user_repo.update_user(user_update_dto)

    @staticmethod
    async def get_user_by_id(user_id: UUID) -> UserDTO | None:
        user_reader = UserRepository()
        return await user_reader.get_user_by_id(user_id)

    @staticmethod
    async def get_user_by_telegram_id(telegram_user_id: int) -> UserDTO | None:
        user_reader = UserRepository()
        return await user_reader.get_user_by_telegram_id(telegram_user_id)
