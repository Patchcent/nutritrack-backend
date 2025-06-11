from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://alexis_user:Patch1552@cluster0.xy1jrsb.mongodb.net/nutritrack?retryWrites=true&w=majority"

client = AsyncIOMotorClient("mongodb+srv://alexis_user:Patch1552@cluster0.xy1jrsb.mongodb.net/nutritrack?retryWrites=true&w=majority")  # AQUÍ creamos el client
db = client["nutritrack"]   # Ya puedes usarlo normalmente
