from fastapi import APIRouter

from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


class HealthCheckResponse(BaseModel):
    success: int
    # master_db: int
    # slave_db: int
    internal_packages: dict = {}


@router.get(
    "/healthcheck",
    responses={200: {"model": HealthCheckResponse}, 500: {"model": HealthCheckResponse}},
)
async def _healthcheck() -> HealthCheckResponse:
    response = HealthCheckResponse(
        success=1,
        # master_db=master_res,
        # slave_db=slave_res,
    )
    status_code = status.HTTP_200_OK if response.success else status.HTTP_500_INTERNAL_SERVER_ERROR
    return JSONResponse(status_code=status_code, content=response.dict())  # type: ignore
