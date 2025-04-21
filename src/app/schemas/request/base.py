from typing import Optional

from pydantic import BaseModel

from app.schemas.request.types import GreatOneInt


class PaginationRequestSchema(BaseModel):
    page: Optional[GreatOneInt] = 1
    limit: Optional[GreatOneInt] = 100
