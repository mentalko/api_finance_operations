from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional, Union

from .constants import OperationKind, OutcomeType, IncomeType


class BaseOperation(BaseModel):
    date: date
    kind: OperationKind
    wallet_id: int
    amount: Decimal
    description: Optional[str]

class OperationIncome(BaseOperation):
    operation_type: Optional[IncomeType]

class OperationOutcome(BaseOperation):
    operation_type: Optional[OutcomeType]



class OperationCreate(OperationIncome, OperationOutcome):

    class Config:
        schema_extra = {
            "example": {
                "date": "2022-10-04",
                "kind": "income",
                "wallet_id": 0,
                "amount": 150_00,
                "description": "My salary for this month",
                "operation_type": "salary"
            }
        }


class OperationUpdate(BaseOperation):
    pass


class Operation(BaseOperation):
    id: int

    class Config:
        orm_mode = True
