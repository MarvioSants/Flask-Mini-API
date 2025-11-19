import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

@patch("requests.get")
def test_usd_to_brl(mock_get, client):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "USDBRL": {"bid": "5.00"}
    }

    response = client.get("/exchange/usd-to-brl?amount=2")
    data = response.get_json()

    assert response.status_code == 200
    assert data["converted"] == 10.0  # 2 × 5.00

@patch("requests.get")
def test_brl_to_usd(mock_get, client):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "BRLUSD": {"bid": "0.20"}
    }

    response = client.get("/exchange/brl-to-usd?amount=10")
    data = response.get_json()

    assert response.status_code == 200
    assert data["converted"] == 2.0  # 10 × 0.2
