from enum import Enum


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class IncomeType(str, Enum):
    Salary = 'salary'
    Cashback = 'cashback'
    refilling = 'refilling'
    Other = 'other'


class OutcomeType(str, Enum):
    Fastfood = 'fastfood'
    Supermakets = 'supermakets'
    Medicine = 'medicine'
    Shopping = 'shopping'
    Transport = 'transport'

    withdrawal = 'withdrawal'
    Other = 'other'


class WalletType(str, Enum):
    cash = 'cash'
    credit_card = 'credit_card'
    # crypto = 'crypto'


class CurrencyFiatCodes(str, Enum):
    usd = 'USD'
    eur = 'EUR'
    gbp = 'GBP'
    rub = 'RUB'
