import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app import app

@pytest.fixture 
def client(): 
    with app.test_client() as client: 
        yield client

def test_home(client): 
    response = client.get('/') 
    assert response.status_code == 200 
    assert response.data == b'Hello, Docker CI/CD!' 