import os
from motor.motor_asyncio import AsyncIOMotorClient
MONGO_URL = "mongodb+srv://alexis_user:Patch1552@cluster0.xy1jrsb.mongodb.net/nutritrack?retryWrites=true&w=majority"

MONGO_URL = os.getenv(MONGO_URL)
db = client.get_default_database()  # Usará 'nutritrack' automáticamente