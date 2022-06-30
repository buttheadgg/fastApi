from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel



class fileoperation(BaseModel):
    id: int
    code: str
    name: str
    date: date

    class Config:
        orm_mode = True