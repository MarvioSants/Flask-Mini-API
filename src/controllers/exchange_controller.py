from flask import Blueprint, jsonify
from src.services.exchange_service import get_usd_to_brl

exchange_bp = Blueprint("exchange", __name__)

@exchange_bp.route("/exchange/usd-to-brl", methods=["GET"])
def usd_to_brl():
    try:
        rate = get_usd_to_brl()
        return jsonify(rate), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
