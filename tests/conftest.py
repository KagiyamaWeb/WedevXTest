import pytest
from app.database import Base, engine
from app.main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope='session')
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(test_db):
    with TestClient(app) as client:
        yield client
