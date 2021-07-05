#-*- coding: utf-8 -*-

from api import api
from sanic import Sanic
from sanic.response import json
from sanic_jwt_extended import JWT
from sanic_cors import CORS
from sanic.exceptions import ServerError
from utilities.exceptions import server_error_handler,expired_signature, no_authorization, invalid_header, invalid_token, jwt_decode_error, revoked_token, wrong_token, fresh_token_required, access_denied

from datetime import datetime, time, timedelta

app = Sanic("Pasarela")
CORS(app, automatic_options=True)

app.config.RESPONSE_TIMEOUT = 45
app.config.REQUEST_TIMEOUT = 45

with JWT.initialize(app) as manager:
    manager.config.use_acl = True
    manager.config.acl_claim = "role"
    manager.config.access_token_expires = timedelta(hours=10)
    manager.config.refresh_token_expires = timedelta(minutes=30)
    manager.config.csrf_protect = True
    manager.config.csrf_request_methods = (
        'POST', 'PUT', 'PATCH', 'DELETE', 'GET')
    manager.config.jwt_csrf_header = 'X-CSRF-Token'
    manager.config.refresh_jwt_csrf_header = 'X-CSRF-Refresh'
    manager.config.secret_key = "AF3A7D8FAC625C9EC90A5D15C265BF7FC793B8E06D0B67A7D675430175B81D57EON[MlO17rwTNTOP"
    manager.config.jwt_header_key = "Authorization"
    manager.config.refresh_jwt_header_key = "X-Refresh"
    manager.handler.expired_signature = expired_signature
    manager.handler.no_authorization = no_authorization
    manager.handler.invalid_header = invalid_header
    manager.handler.invalid_token = invalid_token
    manager.handler.jwt_decode_error = jwt_decode_error
    manager.handler.wrong_token = wrong_token
    manager.handler.revoked_token = revoked_token
    manager.handler.fresh_token_required = fresh_token_required
    manager.handler.access_denied = access_denied

app.blueprint(api)
app.error_handler.add(ServerError, server_error_handler)

ssl = {'cert': '/home/.ssl/midiemo.com.crt',
       'key': '/home/.ssl/new.midiemo.key'}

app.run(debug=False, host="0.0.0.0", port=8000, auto_reload=True)
