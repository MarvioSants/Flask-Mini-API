import pytest
from unittest.mock import patch
from src.controllers.services.exchange_service import get_exchange_rate

@patch("src.controllers.services.exchange_service.requests.get")
def test_get_exchange_rate(mock_get):
    # Simula resposta da API externa
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "BRLUSD": {"bid": "0.20"}
    }

    # Executa o serviço
    result = get_exchange_rate("BRL", "USD")

    # Valida a resposta
    assert result == 0.20
