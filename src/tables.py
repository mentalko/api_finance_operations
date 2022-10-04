import sqlalchemy as sa
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date)
    kind = sa.Column(sa.String)
    wallet_id = sa.Column(sa.Integer)
    amount = sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)
    operation_type = sa.Column(sa.String, nullable=True)




class Wallet(Base):
    __tablename__ = 'wallet'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    type_name = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)
    currency_code = sa.Column(sa.String)