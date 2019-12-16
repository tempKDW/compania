import pytest
from starlette.testclient import TestClient

import models
from database import TestSessionLocal, test_engine
from main import app

client = TestClient(app)
models.Base.metadata.create_all(bind=test_engine)


def get_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_db


@pytest.fixture
def db():
    db = TestSessionLocal()
    yield
    db.query(models.User).delete()
    db.query(models.Interest).delete()


def test_create_user(db):
    response = client.post('/users/', data={'name': 'test', 'password': 'testpw'})

    assert response.status_code == 200
    assert response.json() == {'id': 1,
                               'name': 'test',
                               'is_active': True,
                               'interest': []}


def test_read_user(db):
    client.post('/users/', data={'name': 'test', 'password': 'testpw'})

    response = client.get('/users/1')

    assert response.status_code == 200
    assert response.json() == {'id': 1,
                               'name': 'test',
                               'is_active': True,
                               'interests': []}
