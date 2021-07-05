from sanic import Blueprint
from sanic.request import Request
from sanic_jwt_extended.decorators import jwt_required, jwt_optional
from sanic_jwt_extended.tokens import Token
from ..models import bitcoin

wallet = Blueprint('wallet', '/wallet')


@wallet.route('/balance')
@jwt_required
async def wBalance(request, token: Token):
    return await bitcoin.getWalletBalance(token.identity)

@wallet.route('/convert', methods=['POST'])
async def bitcoinRate(request: Request):
    return bitcoin.exchangeRate(request.json)
