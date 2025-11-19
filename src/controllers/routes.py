from flask import Blueprint, request, jsonify
from services.exchange_service import ExchangeService

exchange_bp = Blueprint('exchange', __name__)
service = ExchangeService()

@exchange_bp.route('/exchange', methods=['GET'])
def exchange():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount'))

    result = service.convert_currency(from_currency, to_currency, amount)
    return jsonify(result), 200
