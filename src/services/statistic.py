from typing import List, Optional
from datetime import datetime
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, query
from sqlalchemy.sql import func, extract, text

from src.models.operations import Operation
from src.models.constants import OperationKind
from src import tables as t
from src.database import get_session

# https://splunktool.com/group-by-year-month-day-in-a-sqlalchemy


class StatisticService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_per_month(self,
                      kind: OperationKind = None,
                      wallet_id: int = None,
                      ) -> List[t.Operation]:

        # TODO: should use temp table or subquery to exclude wallet_id and kind column from result
        query = self.session.query(
            func.to_char(t.Operation.date, 'FMMonth').label("month_name"),
            func.sum(t.Operation.amount).label("month_amount"),
            t.Operation.wallet_id.label("wallet_id"),
            t.Operation.kind.label("kind")
        ).filter(text(f"wallet_id = {wallet_id} AND kind = '{kind}'")) \
            .group_by("month_name", "wallet_id", "kind") \
            .order_by("month_name").limit(12)

        operations = [dict(o) for o in query.all()]
        for o in operations:
            o.pop('kind', None)
            o.pop('wallet_id', None)

        return operations

