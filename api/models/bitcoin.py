# from os import add_dll_directory
from re import T
# from bitcoinlib.transactions import Transaction
from sanic.response import json
from utilities.connection import conn
# from bitcoinlib.wallets import Wallet, wallet_create_or_open, Value
# from bitcoinlib.keys import Key
from cryptos import *
# import cryptotools 
import requests
from bitcoinrpc.authproxy import AuthServiceProxy

CRYPTO_COMPARE = "6ca3675a37a58d178cf8f11456416feb90d5d474f98e7debf2a3d2955505a47e"


rpc_connection = AuthServiceProxy(
    "http://%s:%s@34.72.201.231:18332".format('bitwit', 'bitwit1337'))

# print(rpc_connection.getblockchaininfo())

def createWallet(userName):
    #tb1qm9uxnhpw892ceutzknerzurn89w6gmx6yxrlxq address1
    #tb1qzxc57vz9y4c9uqe7sznx28gvnqr60cdszj9ac5 address2
    pass

async def getWalletBalance(id):
    commands = [ [ "getblockhash", height] for height in range(100) ]
    block_hashes = rpc_connection.batch_(commands)
    blocks = rpc_connection.batch_([["getblock", h] for h in block_hashes])
    block_times = [block["time"] for block in blocks]   
    print(block_hashes)
    print(block_times)


def processTx(user, amount):
    db = conn()
    return True


def exchangeRate(amount):
    newAmount = 0
    r = requests.get(
        'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key={}'.format(CRYPTO_COMPARE))
    rate = r.json()['USD']
    newAmount = amount['data'] / rate
    return json({'data': newAmount, 'type': 'wallet', 'status': 200}, 200)


