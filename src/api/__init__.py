from fastapi import APIRouter
from .operations import router as operations_router
from .statistic import router as statistic_router
from .wallet import router as wallet_router

router = APIRouter()
router.include_router(operations_router, prefix='/operation',  tags=["Operation"])
router.include_router(statistic_router, prefix='/stat', tags=["Statistic"])
router.include_router(wallet_router, prefix='/wallet', tags=["Wallet"])
