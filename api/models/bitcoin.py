import bitcoin
import bitcoinaddress
import secrets

entropy = secrets.randbits(250)
print(entropy)
k = bitcoinaddress.Wallet(testnet=False)
print(k.address)
print(k.key)
print(k.testnet)
