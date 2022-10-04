from typing import List, Optional, Union
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, query

from src.models.operations import OperationCreate, OperationUpdate
from src.models.constants import OperationKind, IncomeType, OutcomeType

from src import tables
from src.database import get_session


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, operation_id: int) -> tables.Operation:
        operation = (
            self.session
            .query(tables.Operation)
            .filter_by(id=operation_id)
            .first()
        )
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def get_list(self,
                 kind: OperationKind = None,
                 operation_type: Union[IncomeType,
                                       OutcomeType] = None,
                 ) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        if operation_type:
            query = query.filter_by(operation_type=operation_type)

        operations = query.all()
        return operations

    def get(self, operation_id: int) -> tables.Operation:
        return self._get(operation_id)

    def create(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        
        # TODO: write sum or substract amount value to Wallet tabble  
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_data: OperationUpdate) -> tables.Operation:
        operation = self._get(operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id: int):
        operation = self._get(operation_id)
        self.session.delete(operation)
        self.session.commit()
