from flask import Flask, request, jsonify
from src.controllers.services.exchange_service import get_exchange_rate

app = Flask(__name__)

@app.get("/exchange/usd-to-brl")
def usd_to_brl():
    amount = float(request.args.get("amount", 1))
    rate = get_exchange_rate("USD", "BRL")
    converted = amount * rate
    return jsonify({
        "base": "USD",
        "target": "BRL",
        "rate": rate,
        "amount": amount,
        "converted": converted
    })

@app.get("/exchange/brl-to-usd")
def brl_to_usd():
    amount = float(request.args.get("amount", 1))
    rate = get_exchange_rate("BRL", "USD")
    converted = amount * rate
    return jsonify({
        "base": "BRL",
        "target": "USD",
        "rate": rate,
        "amount": amount,
        "converted": converted
    })

if __name__ == "__main__":
    app.run(debug=True)
