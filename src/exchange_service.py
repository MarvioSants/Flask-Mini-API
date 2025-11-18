import requests

def get_usd_to_brl():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Erro ao acessar API externa")

    data = response.json()

    # A AwesomeAPI retorna algo como:
    # {
    #   "USDBRL": {
    #      "bid": "5.45"
    #    }
    # }

    return {
        "currency": "USD-BRL",
        "rate": float(data["USDBRL"]["bid"])
    }
