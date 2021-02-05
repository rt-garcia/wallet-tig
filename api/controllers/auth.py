from sanic import Blueprint
from sanic.request import Request
from sanic_jwt_extended.decorators import jwt_required, jwt_optional
from ..models import auth

auth = Blueprint('auth', '/auth')


@auth.route('/signUp', methods=list('POST'))
async def reg(request: Request):
    return True


@auth.route('/signIn', methods=list('POST'))
async def signIn(request: Request):
    return True


@auth.route('/forgot', methods=list('POST'))
async def forgot(request: Request):
    return True


@auth.route('/updateProfile', methods=list('POST'))
async def updateProfile(request: Request):
    return True


@auth.route('/changePassword', methods=list('POST'))
async def changePassword(request: Request):
    return True
