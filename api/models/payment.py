from datetime import datetime
from hashlib import sha256
from utilities.util import generate_qr
from sanic.response import json
from utilities.connection import conn
from . import validator


def generateTraceNumber():
    return str(int(sha256(str(datetime.now()).encode('utf-8')).hexdigest()[:13], 16))


async def createPayment(user, data):
    db = conn()
    isValid = await validator.validPaymentData(user, data)
    if isValid is True:
        data['created_at'] = datetime.now().timestamp()
        data['updated_at'] = datetime.now().timestamp()
        data['status'] = 1
        data['created_by'] = user
        data['payment_id'] = generateTraceNumber()
        data['dir'] = generate_qr(data['payment_id'])
        await db.payments.insert_one(data)
        return json({'data': data['payment_id'], 'type': 'payment', 'status': 200}, 200)
    return isValid


async def confirmPayment(user, data):
    db = conn()
    print(user)
    userInfo = await db.users.find_one({'id': user}, {'_id': 0})
    isValid = await validator.validPaymentConfirmation(userInfo, data)
    if isValid is True:
        await db.payments.update_one({'payment_id': data['payment_id']}, {'$set': {'updated_at': datetime.now().timestamp(), 'status': 2, 'payed_by': user}})
        return json({'data': 'El pago ha sido confirmado con éxito.', 'type': 'payment', 'status': 200}, 200)
    return isValid


async def getPayment(data):
    db = conn()
    pE = await db.payments.find_one({'payment_id': data}, {'_id': 0})
    if pE:
        createdBy = await db.users.find_one({'id': pE['created_by']}, {'_id': 0, 'username': 1} )
        pE['created_by'] = createdBy['username']
        return json({'data': pE, 'type': 'payment', 'status': 200}, 200)
    return json({'data': 'No hemos encontrado un pago asociado a este id.',
          'type': 'payment', 'status': 200}, 200)


async def getAllPayment(user):
    db = conn()
    pE = await db.payments.find({'destiny': user}, {'_id': 0}).to_list(length=10)
    if pE:
        for p in pE:
            createdBy = await db.users.find_one({'id': p['created_by']}, {'_id': 0, 'username': 1})
            p['created_by'] = createdBy['username']
        return json({'data': pE, 'type': 'payment', 'status': 200}, 200)
    return json({'data': [],
                 'type': 'payment', 'status': 200}, 200)
