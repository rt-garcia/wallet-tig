from sanic import Blueprint
from sanic.request import Request
from sanic_jwt_extended.tokens import Token
from sanic_jwt_extended.decorators import jwt_required, jwt_optional

from ..models import auth as A

user  = Blueprint('user', '/user')


@user.route('/signup', methods=['POST'])
async def reg(request: Request):
    return await A.signUp(request.json)


@user.route('/signin', methods=['POST'])
async def signIn(request: Request):
    return await A.signIn(request.json)


@user.route('/forgot', methods=['POST'])
async def forgot(request: Request):
    return await A.forgotPassword(request.json)


@user.route('/update', methods=['PUT'])
@jwt_required
async def updateUser(request: Request, token: Token):
    return await A.updateProfile(request.json, token.identity)


@user.route('/<id>', methods=['GET', 'DELETE'])
@jwt_optional
async def getUser(request: Request, token: Token, id):
    if request.method == 'DELETE':
        return await A.deactivateUser(id)
    else:
        if token:
            return await A.getUser(token.identity)
        elif id:
            return await A.getUser(id)


@user.route('/changePassword', methods=['POST'])
@jwt_optional
async def changePassword(request: Request, token: Token):
    return await A.changePassword(token, request.json)


@user.route('/userExist', methods=['POST'])
async def userE(request: Request):
    return await A.userExist(request.json)

@user.route('/countries')
async def countriesList(request: Request):
    return await A.getCountries()


