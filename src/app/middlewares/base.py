from fastapi import FastAPI
from uuid import uuid4

from loguru import logger

from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.middleware import is_valid_uuid4
from starlette.middleware.cors import CORSMiddleware


def setup_middlewares(app: FastAPI, request_id_len: int = 8):
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex='.*',
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=['X-Request-ID'],
    )
    logger.info("Setup %s middleware", CORSMiddleware)

    app.add_middleware(
        CorrelationIdMiddleware,
        header_name='X-Request-ID',
        update_request_header=True,
        generator=lambda: uuid4().hex,
        validator=is_valid_uuid4,
        transformer=lambda a: str(a)[:request_id_len],
    )
    logger.info("Setup %s middleware", CorrelationIdMiddleware)
