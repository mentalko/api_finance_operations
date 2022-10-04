from typing import List, Optional
from fastapi import APIRouter
from fastapi import Depends, Response, status

from src import tables
from src.database import get_session
from src.models.constants import WalletType
from src.models.wallet import Wallet, SafeBox
from src.services.wallet import WalletsService

router = APIRouter()


@router.get('', response_model=List)
def get_wallets(
    kind: Optional[WalletType] = None,
    service: WalletsService = Depends()
):
    return service.get_list(kind=kind)


@router.post("/create", response_model=List)
def create_wallet(
        Wallet_data: Wallet,
        service: WalletsService = Depends()
):
    return service.get_list(kind=kind)

@router.post("/create_savebox", response_model=List)
def create_savebox(
    safebox_data: SafeBox, 
    service: WalletsService = Depends()
):
    pass