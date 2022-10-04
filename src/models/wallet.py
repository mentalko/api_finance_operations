from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional, Union

from .constants import WalletType, CurrencyFiatCodes


class BaseWallet(BaseModel):
    title: str
    type_name: WalletType
    amount: Decimal
    description: Optional[str]

class Wallet(BaseWallet):
    currency_code: CurrencyFiatCodes


class SafeBox(Wallet):
    goal: Decimal


class WalletCreate(Wallet):

    class Config:
        schema_extra = {
            "example": {
                "title": "My credit card",
                "type_name": "credit_card",
                "amount": 150_000,
                "description": "My salary for this month",
                "operation_type": "salary"
            }
        }




class Wallet(BaseWallet):
    id: int

    class Config:
        orm_mode = True
