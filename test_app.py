import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Abdul Wahab" in response.data
