from sanic.response import json
from sanic_jwt_extended import JWT
from utilities.util import forgotCode
from utilities.connection import conn
from utilities.exceptions import invalid_password_or_username

from smtp.smtp import send
from smtp.templates import forgotPwTemplate, loginTemplate, signupTemplate
from . import validator, bitcoin
from uuid import uuid4


'''
AUTHENTICATION
'''
async def signIn(data):
    isValid = validator.validateSignInData(data)
    if isValid is True:
        db = conn()
        uE = await db.users.find_one({'username': data['username']}, {'_id': 0})
        if uE:
            # wal = await db.wallets.find_one({'id': uE['id']}, {'_id': 0})
            if uE['password'] == data['password']:
                res = {
                      'user':{
                        'user': uE['username'],
                        'fullname': uE['first_name'] + uE['last_name'],
                        'role': uE['role'],
                        # 'address': wal['wallet']['address'],
                    },  
                    'token': JWT.create_access_token(identity=uE['id'], role=uE['role'])
                }
                send(uE['email'], '¡Has iniciado sesión!', loginTemplate(uE['first_name']+' '+uE['last_name']))
                return json({'data': res, 'type': 'success','code': 200}, 200)
            else:
                return invalid_password_or_username()
        else:
           return await commercesignin(data)
    return isValid


async def signUp(data):
    isValid = validator.validateSignUpData(data)
    if isValid is True:
        db = conn()
        userId =  str(uuid4())
        data['role'] = 'user'
        data['id'] = userId
        data['full_name'] = (data['first_name'] + data['last_name']).title()
        wallet = bitcoin.createWallet(userId)
        send(data['email'], '¡Bienvenido!', signupTemplate(data['first_name']+' '+data['last_name']))
        await db.users.insert_one(data)
        await db.wallets.insert_one(wallet)
        return json({'data': '¡Usuario registrado con éxito!', 'type': 'success', 'code': 200}, 200)
    return isValid


async def commerceSignUp(data):
    isValid = validator.validateCommerceSignUpData(data)
    # isValid = True
    if isValid is True:
        db = conn()
        userId = str(uuid4())
        data['role'] = 'company'
        data['id'] = userId
        # data['wallet'] = bitcoin.createWallet(data)
        # send(data['email'], '¡Bienvenido!', signupTemplate(
        #     data['commerce_name'])) 
        await db.commerces.insert_one(data)
        return json({'data': '¡Comercio registrado con éxito!', 'type': 'success', 'code': 200}, 200)
    return isValid


async def commercesignin(data):
    isValid = validator.validateSignInData(data)
    if isValid is True:
        db = conn()
        uE = await db.commerces.find_one({'username': data['username']}, {'_id': 0})
        if uE:
            # wal = await db.wallets.find_one({'id': uE['id']}, {'_id': 0})
            if uE['password'] == data['password']:
                res = {
                    'user': {
                        'user': uE['username'],
                        'fullname': uE['company_name'],
                        'role': uE['role'],
                        # 'address': wal['wallet']['address'],
                    },
                    'token': JWT.create_access_token(identity=uE['id'], role=uE['role'])
                }
                send(uE['company_email'], '¡Has iniciado sesión!',
                     loginTemplate(uE['company_name']))
                return json({'data': res, 'type': 'success', 'code': 200}, 200)
            else:
                return invalid_password_or_username()
        else:
            return invalid_password_or_username()
    return isValid


async def forgotPassword(data):
    emailExist = validator.validForgotRequest(data)
    if emailExist:
        send(data['email'], '¡Recupera tu contraseña!', forgotPwTemplate(forgotCode()))
    return emailExist


async def changePassword(token, data):
    db = conn()
    if token:
        await db.users.update_one({'username': token.identity}, {'$set':{'password': data['new_password']}})
        return json({'data': '¡Contraseña cambiada con éxito!', 'type': 'success', 'code': 200}, 200)
    else:
        isValid = validator.validForgotRequest(data['email'])
        if isValid:
            await db.users.update_one({'username': data['email']}, {'$set':{'password': data['new_password']}})
            return json({'data': '¡Contraseña cambiada con éxito!', 'type': 'success', 'code': 200}, 200)
        return isValid  


async def updateProfile(data, user):
    return json({'data': '¡Usuario modificado con éxito!', 'type': 'success', 'code': 200}, 200)


async def updateCommerceProfile(data, user):
    return json({'data': '¡Comercio modificado con éxito!', 'type': 'success', 'code': 200}, 200)


async def userExist(data):
    db = conn()
    if not await db.users.find_one({'username': data['data']}):
        return json({'data': False, 'type': 'success', 'code': 200}, 200)
    return json({'data': True, 'type': 'success', 'code': 200}, 200)


async def getCountries():
    db = conn()
    c =  await db.countries.find({}, {'_id': 0}).to_list(length=None)
    return json({'data': c, 'type': 'auth', 'code': 200})


async def getUser(id):
    db = conn()
    uE = await db.users.find_one({'id': id}, {'_id': 0})
    if uE:
        return json({'data': uE, 'type': 'success', 'code': 200}, 200)
    else:
        return json({'data': None, 'type': 'success', 'code': 200}, 200)


async def getCommerce(id):
    db = conn()
    uE = await db.commerces.find_one({'id': id}, {'_id': 0})
    if uE:
        return json({'data': uE, 'type': 'success', 'code': 200}, 200)
    else:
        return json({'data': None, 'type': 'success', 'code': 200}, 200)


async def deactivateUser(id):
    db = conn()
    await db.users.find_one_and_update({'id': id}, {'$set': {'is_active': False}})
    return json({'data': '¡Usuario desactivado exitosamente!', 'type': 'success', 'code': 200}, 200)


async def deactivateCommerce(id):
    db = conn()
    await db.commerces.find_one_and_update({'id': id}, {'$set': {'is_active': False}})
    return json({'data': 'Comercio desactivado exitosamente!', 'type': 'success', 'code': 200}, 200)
