from motor.motor_asyncio import AsyncIOMotorClient

URI = "mongodb://localhost:27017/pasarela"

def conn():
    client = AsyncIOMotorClient(URI)
    return client['pasarela']