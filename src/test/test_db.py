import motor.motor_asyncio
import asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
print("Conexión exitosa:", client)

async def list_dbs():
    db_list = await client.list_database_names()
    print("Bases de datos:", db_list)

if __name__ == "__main__":
    asyncio.run(list_dbs())