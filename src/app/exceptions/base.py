from enum import Enum
from fastapi import status


class ExceptionEnum(Enum):
    @property
    def error(self):
        return self.value[0]

    @property
    def error_fields(self):
        return self.value[1]


class BaseAppException(Exception):
    error: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_fields: dict | None = None

    def __init__(self, error_fields: dict | None = None):
        super().__init__(error_fields)
        self.error_fields = error_fields


class BaseBadRequestException(BaseAppException):
    "Запрос не удалось обработать из-за синтаксической ошибки"
    error: int = status.HTTP_400_BAD_REQUEST


class BaseAuthException(BaseAppException):
    "Ошибка авторизации"
    error: int = status.HTTP_401_UNAUTHORIZED


class BasePaymentRequiredException(BaseAppException):
    "Ошибка доступа к платному контенту"
    error: int = status.HTTP_402_PAYMENT_REQUIRED


class BaseForbiddenException(BaseAppException):
    "Доступ запрещен"
    error: int = status.HTTP_403_FORBIDDEN


class BaseNotFoundException(BaseAppException):
    "Объект не найден"
    error: int = status.HTTP_404_NOT_FOUND


class BaseMethodNotAllowedException(BaseAppException):
    "Выполнение метода не разрешено"
    error: int = status.HTTP_405_METHOD_NOT_ALLOWED


class BaseNotAcceptableException(BaseAppException):
    "Запрос выполняется слишком рано"
    error: int = status.HTTP_406_NOT_ACCEPTABLE


class BaseConflictException(BaseAppException):
    "Запрос нельзя обработать из-за конфликта"
    error: int = status.HTTP_409_CONFLICT


class BaseIncorrectValueException(BaseAppException):
    "Ошибка валидации. Неправильное значение"
    error: int = status.HTTP_422_UNPROCESSABLE_ENTITY


class BaseFailedDependencyException(BaseAppException):
    "Нарушение связанности"
    error: int = status.HTTP_424_FAILED_DEPENDENCY


class BaseRequiredParamIsMissingException(BaseAppException):
    "Ошибка валидации. Требуемый параметр отсутствует"
    error: int = status.HTTP_428_PRECONDITION_REQUIRED
