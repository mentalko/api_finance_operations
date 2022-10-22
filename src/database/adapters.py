from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyUserDatabase

from src.database.db import get_async_session
from src.database.tables import User


async def get_user_adapter(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)