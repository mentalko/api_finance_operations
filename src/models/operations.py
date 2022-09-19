from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional

from .constants import OperationKind

class BaseOperation(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]


class OperationCreate(BaseOperation):
    pass


class OperationUpdate(BaseOperation):
    pass

class Operation(BaseOperation):
    id: int
    
    class Config:
        orm_mode = True