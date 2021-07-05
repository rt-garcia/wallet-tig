from utilities.connection import conn
from utilities.exceptions import invalid_data_type
from sanic.response import json
from sanic.log import logger
from .bitcoin import getWalletBalance, exchangeRate

def validateSignInData(data):
    if not 'username' in data:
        return json({'data': "Key 'username' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'password' in data:
        return json(({'data': "Key 'password' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500))
    if not isinstance(data['username'], str):
        return invalid_data_type(data['username'])
    if not isinstance(data['password'], str):
        return invalid_data_type(data['password'])
    return True


def validateSignUpData(data):
    if not 'first_name' in data:
        return json({'data': "Key 'first_name' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'last_name' in data:
        return json({'data': "Key 'last_na,e' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'phone_number' in data:
        return json({'data': "Key 'phone_number' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    # if not 'address1' in data:
    #     return json({'data': "Key 'address1' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    # if not 'address2' in data:
    #     return json({'data': "Key 'address2' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'country' in data:
        return json({'data': "Key 'country' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'email' in data:
        return json({'data': "Key 'email' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    # if not 'city' in data:
    #     return json({'data': "Key 'city' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    # if not 'postal_code' in data:
    #     return json({'data': "Key 'postal_code' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'username' in data:
        return json({'data': "Key 'username' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'password' in data:
        return json({'data': "Key 'password' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not isinstance(data['first_name'], str):
        return invalid_data_type('first_name')
    if not isinstance(data['last_name'], str):
        return invalid_data_type('last_name')
    if not isinstance(data['phone_number'], str):
        return invalid_data_type('phone_number')
    if not isinstance(data['address1'], str):
        return invalid_data_type('addres1')
    if not isinstance(data['address2'], str):
        return invalid_data_type('address2')
    if not isinstance(data['country'], str):
        return invalid_data_type('country')
    if not isinstance(data['state'], str):
        return invalid_data_type('state')
    if not isinstance(data['postal_code'], str):
        return invalid_data_type('postal_code')
    if not isinstance(data['username'], str):
        return invalid_data_type('username')
    if not isinstance(data['password'], str):
        return invalid_data_type('password')
    if not isinstance(data['email'], str):
        return invalid_data_type('email')
    return True


def validateCommerceSignUpData(data):
    if not 'company_name' in data:
        return json({'data': "Key 'company_name' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'company_rif' in data:
        return json({'data': "Key 'company_rif' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'company_email' in data:
        return json({'data': "Key 'company_email' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'company_phone' in data:
        return json({'data': "Key 'company_phone' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'contact_first_name' in data:
        return json({'data': "Key 'contact_first_name' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'contact_last_name' in data:
        return json({'data': "Key 'contact_last_name' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'contact_phone_number' in data:
        return json({'data': "Key 'contact_phone_number' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'contact_dni' in data:
        return json({'data': "Key 'contact_dni' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'address1' in data:
        return json({'data': "Key 'address1' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'address2' in data:
        return json({'data': "Key 'address2' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'country' in data:
        return json({'data': "Key 'country' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'state' in data:
        return json({'data': "Key 'state' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'postal_code' in data:
        return json({'data': "Key 'postal_code' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'username' in data:
        return json({'data': "Key 'username' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not 'password' in data:
        return json({'data': "Key 'password' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not isinstance(data['company_name'], str):
        return invalid_data_type(data['company_name'])
    if not isinstance(data['company_email'], str):
        return invalid_data_type(data['company_email'])
    if not isinstance(data['company_phone'], str):
        return invalid_data_type(data['company_phone'])
    if not isinstance(data['company_rif'], str):
        return invalid_data_type(data['company_rif'])
    if not isinstance(data['contact_first_name'], str):
        return invalid_data_type(data['first_name'])
    if not isinstance(data['contact_last_name'], str):
        return invalid_data_type(data['last_name'])
    if not isinstance(data['contact_phone_number'], str):
        return invalid_data_type(data['contact_phone_number'])
    if not isinstance(data['address1'], str):
        return invalid_data_type(data['addres1'])
    if not isinstance(data['address2'], str):
        return invalid_data_type(data['address2'])
    if not isinstance(data['country'], str):
        return invalid_data_type(data['country'])
    if not isinstance(data['state'], str):
        return invalid_data_type(data['state'])
    if not isinstance(data['postal_code'], str):
        return invalid_data_type(data['postal_code'])
    if not isinstance(data['username'], str):
        return invalid_data_type(data['username'])
    if not isinstance(data['password'], str):
        return invalid_data_type(data['password'])
    return True


def validForgotRequest(email):
    db = conn()
    if not 'email' in email:
        return json({'data': "Key 'email' no encontrado en el payload.", 'type': 'error', 'code': 502}, 500)
    if not db.users.find_one({'email': email}):
        return json({'data': "El email que has ingresado no se encuentra", 'type': 'error', 'code': 502}, 500)
    else:
        return True


async def validPaymentData(user, data):
    db = conn()
    destiny = await db.users.find_one({'username': data['destiny']}, {'_id': 0, 'id': 1})
    if not destiny:
        return json({'data': "El usuario destino es inválido o no existe.", 'type': 'payment', 'code': 503}, 500)
    if data['amount'] < 0.0:
        return json({'data': "Este no es un monto válido.", 'type': 'payment', 'code': 503}, 500)
    if destiny == user:
        return json({'data': "El usuario destino es inválido o no existe.", 'type': 'payment', 'code': 503}, 500)
    return True


async def validPaymentConfirmation(userInfo, data):
    db = conn()
    paymentExist = await db.paymentstw.find_one({'payment_id': data['payment_id']}, {'_id': 0})
    if data['confirmation']:
        if paymentExist and paymentExist['status'] == 1:
            # if getWalletBalance(paymentExist['destiny']) > paymentExist['amount']:
                logger.info("Pago validado, ajustando balances tanto del emisor como receptor.")
                return True
            # return json({'data': "No posee suficientes fondos para realizar el pago.", 'type': 'payment', 'code': 503}, 500)
        return json({'data': "El pago no existe o ya se encuentra en un estado final (pagado o rechazado).", 'type': 'payment', 'code': 503}, 500)
    return json({'data': "El pago ha sido rechazado por el receptor.", 'type': 'payment', 'code': 503}, 500)


# async def adjustBalances(emisor, receptor, monto):
#     db = conn()
#     await db.wallets.find_one_and_update({'id': emisor}, {'$inc': {'balance': monto}})
#     await db.wallets.find_one_and_update({'id': receptor}, {'$inc': {'balance': -monto}})
#     logger.info("Balances modificados")
#     return True
