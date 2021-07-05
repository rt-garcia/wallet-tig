from sanic import Blueprint
from sanic.request import Request
from sanic_jwt_extended import tokens
from sanic_jwt_extended.decorators import jwt_required, jwt_optional
from sanic_jwt_extended.tokens import Token
from ..models import payment as p


payment = Blueprint('payment', '/payment')


@payment.route('/charge',['POST'])
@jwt_required
async def charge(request: Request, token: Token):
    return await p.createPayment(token.identity, request.json)


@payment.route('/pay', ['POST'])
@jwt_required
async def charge(request: Request, token: Token):
    return await p.confirmPayment(token.identity, request.json)


@payment.route('/<id>')
@jwt_required
async def getPayment(request: Request, token: Token, id):
    return await p.getPayment(id)


@payment.route('/all')
@jwt_required
async def getAllPayments(request: Request, token: Token):
    return await p.getAllPayment(token.identity)


@payment.route('/listCharges', ['POST'])
@jwt_required
async def listB(request: Request):
    return True


@payment.route('/listDebits', ['POST'])
@jwt_required
async def listB(request: Request):
    return True


@payment.route('/listPending', ['POST'])
@jwt_required
async def listB(request: Request):
    return True
