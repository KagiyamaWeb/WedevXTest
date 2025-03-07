import pytest

from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, Base, engine


@pytest.fixture(scope='module')
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_create_project(client):
    response = client.post('/projects/', json={
        'project_name': 'Office Building',
        'location': 'New York'
    })
    assert response.status_code == 200
    data = response.json()
    assert data['project_name'] == 'Office Building'
    assert len(data['tasks']) > 0
    assert data['status'] == 'processing'


def test_get_project(client, test_db):
    # First create a project
    create_resp = client.post('/projects/', json={
        'project_name': 'Test Project',
        'location': 'Test Location'
    })
    project_id = create_resp.json()['id']
    
    # Test retrieval
    response = client.get(f'/projects/{project_id}')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == project_id
    assert data['status'] == 'processing'

def test_invalid_project_id(client):
    response = client.get('/projects/9999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Project not found'
