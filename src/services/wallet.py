from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, query

from src.models.wallet import WalletCreate
from src.models.constants import WalletType

from src import tables
from src.database import get_session 

class WalletsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, wallet_id: int) -> tables.Wallet:
        wallet = (
            self.session
            .query(tables.Wallet)
            .filter_by(id=wallet_id)
            .first()
        )
        if not wallet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return wallet

    def get_list(self, kind: WalletType=None) -> List[tables.Wallet]:
        query = self.session.query(tables.Wallet)
        if kind:
            query = query.filter_by(type_name=kind)
        wallets = query.all()
        return wallets

    def get(self, wallet_id: int) -> tables.Wallet:
        return self._get(wallet_id)
       

    def create(self, wallet_data: WalletCreate) -> tables.Wallet:
        wallet = tables.Wallet(**wallet_data.dict())
        self.session.add(wallet)
        self.session.commit()
        return wallet
        

