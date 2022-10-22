from typing import List, Optional
from fastapi import APIRouter
from fastapi import Depends, Response, status

from src.database.tables import User
from src.models.users import UserRead, UserCreate, UserUpdate
from src.services.users import fast_api_users as fastapi_users, auth_backend

# from src import tables
# from src.database import get_session
# from src.models.constants import WalletType
# from src.models.wallet import Wallet, SafeBox
# from src.services.wallet import WalletsService

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
router.include_router(fastapi_users.get_reset_password_router())
router.include_router(fastapi_users.get_verify_router(UserRead))
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))


# @router.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}

