from typing import List, Optional, Union
from fastapi import APIRouter
from fastapi import Depends, Response, status

from src import tables 
from src.database import get_session
from src.models.operations import Operation, OperationCreate, OperationUpdate
from src.models.constants import  OperationKind, IncomeType, OutcomeType
from src.services.operations import OperationsService

router = APIRouter()

@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    operation_type: Optional[Union[IncomeType, OutcomeType]] = None,
    service: OperationsService = Depends()
):
    return service.get_list(kind=kind, operation_type=operation_type)

@router.post('/', response_model=Operation)
def create_operation(
    operation_data: OperationCreate,
    service: OperationsService = Depends()
):
    return service.create(operation_data)

@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int, 
    service: OperationsService = Depends()
):
    return service.get(operation_id)

@router.put('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    service: OperationsService = Depends()
):
    return service.update(
        operation_id,
        operation_data,
    )

@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    service: OperationsService = Depends()
):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)