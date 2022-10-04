from typing import List, Optional
from fastapi import APIRouter
from fastapi import Depends, Response, status

from src import tables
from src.database import get_session
from src.models.operations import Operation, OperationCreate, OperationKind, OperationUpdate
from src.services.statistic import StatisticService

router = APIRouter()

# GET spending per month


@router.get('/yearly',
            response_model=List,
            summary="Yearly statistic income/outcome",
            status_code=status.HTTP_200_OK)
def get_per_month(
    kind: OperationKind = None,
    wallet_id: int = None,
    service: StatisticService = Depends()
):
    return service.get_per_month(kind=kind, wallet_id=wallet_id)


@router.get('/history', response_model=List)
def get_history():
    pass
