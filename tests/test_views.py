from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

def test_add_success():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [3, 7]

def test_add_invalid_payload():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [1, 2]})
    assert response.status_code == 422

def test_add_empty_payload():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": []})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == []

def test_add_error_handling():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[1, "two"], [3, 4]]})
    assert response.status_code == 422
