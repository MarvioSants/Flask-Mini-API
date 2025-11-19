from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.get("/exchange/usd-to-brl")
def usd_to_brl():
    amount = float(request.args.get("amount", 1))

    # Chamada da API externa
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Erro ao buscar cotação"}), 500

    data = response.json()
    rate = float(data["USDBRL"]["bid"])  # Cotação real

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

    url = "https://economia.awesomeapi.com.br/json/last/BRL-USD"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Erro ao buscar cotação"}), 500

    data = response.json()
    rate = float(data["BRLUSD"]["bid"])

    converted = amount * rate

    return jsonify({
        "base": "BRL",
        "target": "USD",
        "rate": rate,
        "amount": amount,
        "converted": converted
    })

@app.route("/")
def home():
    return {"message": "API rodando! Use /exchange para conversão."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
