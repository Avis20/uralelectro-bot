from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

# from loguru import logger

# from app.exceptions import base as app_exceptions


def setup_error_handlers(app: FastAPI):
    ...
    # app.add_exception_handler(app_exceptions.BaseAppException, application_exception_handler)  
    # logger.info("Setup %s error handler", app_exceptions.BaseAppException)
    # app.add_exception_handler(AsyncHTTPXResponseError, http_exception_handler)  
    # logger.info("Setup %s error handler", AsyncHTTPXResponseError)
