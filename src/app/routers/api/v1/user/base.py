from uuid import UUID
from fastapi import APIRouter, status
import logging

from app.dependencies import UserServiceDep
from app.schemas.response.base import ResponseSchema
from app.schemas.request.user import UserCreateSchema, UserUpdateSchema
from app.schemas.response.user import UserResponseSchema, UserItemResponseSchema


router = APIRouter(prefix="/user", tags=["Users"])

logger = logging.getLogger()


@router.post(
    '/add',
    summary="Добавление объекта",
    description="Создание нового объекта",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema,
)
async def _add_user(
    request_user: UserCreateSchema,
    user_service: UserServiceDep,
):
    user_dto = await user_service.create_user(request_user)
    return UserResponseSchema(success=1, item=UserItemResponseSchema(**user_dto.as_dict()))


@router.get(
    '/{user_id}/get',
    summary="Получение объекта",
    description="Получение созданного объекта",
    response_model=UserResponseSchema,
)
async def _get_user(
    user_id: UUID,
    user_service: UserServiceDep,
):
    user_dto = await user_service.get_user(user_id)
    return UserResponseSchema(success=1, item=UserItemResponseSchema(**user_dto.as_dict()))


@router.post(
    '/{user_id}/update',
    summary="Изменение объекта",
    description="Изменение объекта",
    response_model=UserResponseSchema,
)
async def _user_update(
    user_id: UUID,
    request_user: UserUpdateSchema,
    user_service: UserServiceDep,
):
    user_dto = await user_service.user_update(request_user, user_id)
    return UserResponseSchema(success=1, item=UserItemResponseSchema(**user_dto.as_dict()))


@router.delete(
    '/{user_id}/delete',
    summary="Удаление объекта",
    description="Удаление созданной объекта",
    response_model=ResponseSchema,
)
async def _delete_user(
    user_id: UUID,
    user_service: UserServiceDep,
):
    await user_service.delete_user(user_id)
    return ResponseSchema(success=1)
