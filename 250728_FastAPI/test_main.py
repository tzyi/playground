import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello, World!"

def test_post_data():
    response = client.post("/data", json={"key": "value"})
    assert response.status_code == 200
    assert response.text == "Received"
