from bitcoinrpc.authproxy import AuthServiceProxy

rpc_connection = AuthServiceProxy(
    "http://{}:{}@34.72.201.231:18332".format('bitwit', 'bitwit1337'))

commands = [
    # ['getnewaddress']
    ["listunspent", 1, 9999999, ["tb1qd06s2uzwm645dmjdy4n7d4mtqzrx6dwd73vut7"]]
]

c = rpc_connection.batch_(commands)     
print(c)

commands = [
    ['createrawtransaction', [{
        "txid": 'dcb33097806963f72a6fee6e52a31f5d36bd1126e94079b2a4ef29ba0b36203d',
        'vout': 1
    }], {
        "tb1qd06s2uzwm645dmjdy4n7d4mtqzrx6dwd73vut7": 0.00041930, "tb1q6w7dlf35sfj23sldrasek8jxvc3uczjdangv3n": 0.00000030
    }]
]

c = rpc_connection.batch_(commands)

commands = [
    ['signrawtransactionwithwallet', c[0]]
]

c = rpc_connection.batch_(commands)
print(c[0])
