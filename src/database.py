from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session

from src.settings import settings

engine = create_engine(
    settings.database_url,
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)

def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()