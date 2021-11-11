from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum

class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


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