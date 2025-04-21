from pydantic import BaseModel, Field


class ResponseSchema(BaseModel):
    success: int = 0
    params: dict = Field(default_factory=dict)
