from sanic import Blueprint
from sanic.request import Request
from sanic_jwt_extended.tokens import Token
from sanic_jwt_extended.decorators import jwt_required, jwt_optional

from ..models import auth as A

commerce = Blueprint('commerce', '/commerce')


@commerce.route('/signup', methods=['POST'])
async def cReg(request: Request):
    return await A.commerceSignUp(request.json)


@commerce.route('/signin', methods=['POST'])
async def cReg(request: Request):
    return await A.commercesignin(request.json)


@commerce.route('/update', methods=['PUT'])
@jwt_required
async def cReg(request: Request, token: Token):
    return await A.updateCommerceProfile(request.json, token.identity)


@commerce.route('/<id>', methods=['GET', 'DELETE'])
@jwt_optional
async def commerceG(request: Request, token: Token, id):
    if request.method == 'DELETE':
        return await A.deactivateCommerce(id)
    return await A.getCommerce(id)
