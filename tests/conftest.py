import pytest
import logging

from fastapi.testclient import TestClient
from src.app import app


LOGGER = logging.getLogger(__name__)

class tmp:
    operation_id = None


@pytest.fixture(autouse=True, scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client