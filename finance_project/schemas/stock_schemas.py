"""Schemas for Stock API. """

from pydantic import BaseModel


class StockSchema(BaseModel):
    name: str
    price: int
    code: str
