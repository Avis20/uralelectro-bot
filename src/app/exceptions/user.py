from app.exceptions import base as app_exceptions


class UserException(app_exceptions.BaseAppException):
    class UserExistsException(app_exceptions.BaseConflictException):
        pass

    class UserNotFoundException(app_exceptions.BaseNotFoundException):
        pass

    class UserForbiddenException(app_exceptions.BaseForbiddenException):
        pass
