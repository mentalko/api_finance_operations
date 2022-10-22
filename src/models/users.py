import uuid
from fastapi_users import schemas

class UserRead(schemas.BaseUser[uuid.UUID]):
    first_name: str
    phone_number: str 

class UserCreate(schemas.BaseUserCreate):
    first_name: str
    phone_number: str 

class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    phone_number: str