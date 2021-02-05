from sanic_jwt_extended.exceptions import *
from sanic import request
from sanic import response


async def server_error_handler(request: request.Request, exception):
    return response.json({'message': exception, 'request': request.body}, 500)

async def expired_signature(request: request.Request, exception: JWTExtendedException):
    message = "Expired Signature"
    code = 211
    return response.json({'message': message, 'code': code}, 500)


async def no_authorization(request: request.Request, exception: JWTExtendedException):
    message = "No authorization header"
    code = 201
    return response.json({'message': message, 'code': code}, 500)


async def invalid_header(request: request.Request, exception: JWTExtendedException):
    message = "Invalid authorization header"
    code = 202
    return response.json({'message': message, 'code': code}, 500)


async def invalid_token(request: request.Request, exception: JWTExtendedException):
    message = "Invalid authorization token"
    code = 203
    return response.json({'message': message, 'code': code}, 500)


async def jwt_decode_error(request: request.Request, exception: JWTExtendedException):
    message = "JWT Decoding error"
    code = 204
    return response.json({'message': message, 'code': code}, 500)


async def wrong_token(request: request.Request, exception: JWTExtendedException):
    message = "Wrong authorization token"
    code = 205
    return response.json({'message': message, 'code': code}, 500)


async def revoked_token(request: request.Request, exception: JWTExtendedException):
    message = "Revoked token"
    code = 206
    return response.json({'message': message, 'code': code}, 500)


async def fresh_token_required(request: request.Request, exception: JWTExtendedException):
    message = "Fresh token is required"
    code = 207
    return response.json({'message': message, 'code': code}, 500)


async def access_denied(request: request.Request, exception: JWTExtendedException):
    message = "Access denied"
    code = 208
    return response.json({'message': message, 'code': code}, 500)
