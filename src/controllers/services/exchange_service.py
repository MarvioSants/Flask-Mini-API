import requests

class ExchangeService:
    def convert_currency(self, from_currency, to_currency, amount):
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

        response = requests.get(url)
        data = response.json()

        if "rates" not in data or to_currency not in data["rates"]:
            raise ValueError("Moeda inválida")

        rate = data["rates"][to_currency]
        converted_value = amount * rate

        return {
            "from": from_currency,
            "to": to_currency,
            "rate": rate,
            "original_amount": amount,
            "converted_amount": round(converted_value, 2)
        }
