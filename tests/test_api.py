import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_check(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_analyze_endpoint(client):
    response = client.post('/api/analyze', 
                          json={'text': 'Turmeric has bitter taste and hot potency.'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert 'results' in data
