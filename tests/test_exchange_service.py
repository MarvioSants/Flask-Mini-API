from unittest.mock import patch
from src.services.exchange_service import get_usd_to_brl

@patch("src.exchange_service.requests.get")
def test_get_usd_to_brl(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "USDBRL": {
            "bid": "5.50"
        }
    }

    result = get_usd_to_brl()

    assert result["currency"] == "USD-BRL"
    assert result["rate"] == 5.50
