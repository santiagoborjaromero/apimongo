# from src.config.settings import get_settings
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

HOST="172.20.0.4"
PORT=27017
USER="lisahadmin"
CLS="L1s4hUn14nd3s"
DATABASE_NAME="lisah"
AUTH_SOURCE = DATABASE_NAME

# settings = get_settings()
# conn = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
# conn = AsyncIOMotorClient(f"mongodb://{MONGO_URI}/", username=USER, password=PASS, authSource="admin")
# conn = AsyncIOMotorClient(host=HOST,port=PORT,username=USER, password=PASS, authSource=AUTH_SOURCE)
MONGO_URI = f"mongodb://{USER}:{CLS}@{HOST}:{PORT}/?authSource={AUTH_SOURCE}"
try:
    conn = AsyncIOMotorClient(MONGO_URI)
    print(conn)
except Exception as e:
    print("❌ Error:", e)
finally:
    db = conn[DATABASE_NAME] 
    
# await conn.lisah.command('ping')
# # db = conn[settings.DATABASE_NAME] 
# db = conn[DATABASE_NAME] 
# print(db)
# print(f"Conexión exitosa {HOST}:{PORT}/{DATABASE_NAME}")
