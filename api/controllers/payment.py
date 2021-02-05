from sanic import Blueprint
from sanic_jwt_extended.decorators import jwt_required, jwt_optional

payment = Blueprint('payment', '/payment')
