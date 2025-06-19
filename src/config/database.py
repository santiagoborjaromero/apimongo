from src.config.settings import get_settings
import motor.motor_asyncio
settings = get_settings()
conn = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
db = conn[settings.DATABASE_NAME] 
print(f"Conexión exitosa {settings.MONGO_URI}/{settings.DATABASE_NAME}")
