from fastapi.responses import JSONResponse
from fastapi import Security
from fastapi.security import APIKeyHeader
from datetime import  datetime, timedelta, timezone
from fastapi.responses import JSONResponse
# from bson import json_util
import json
from src.utils.descrypter import decrypt

def errorHandler(e):
    msgerr = ""
    if hasattr(e, 'message'):
        msgerr = e.message
    else:
        if str(e) == "'NoneType' object is not subscriptable":
            msgerr = "No se encuentra la informacion solicitada"
        else:
            msgerr = str(e)
    return msgerr


def formatResponse(stat: int, object: str | list[str]):
    if stat == 1:
        if object == None:
            object = []

        status = True
        message = ""  
        data = object

    else:
        status = False
        message = object
        data = []
    

    return JSONResponse({"status": status, "message": message, "data": data})


def get_ws_origin(api_key: str = Security(APIKeyHeader(name='Authorization'))):
    return api_key

def sendTokenData(api_key:str):
    tokenOriginal = api_key.split(" ")[1]
    return tokenOriginal

def getTokenData(api_key:str):
    tokenOriginal = api_key.split(" ")[1]
    dToken = json.loads(validate_token(tokenOriginal))
    return dToken

def validate_token(token):
    jwt = ""
    try:
        jwt = decrypt(token)
        # print(jwt)
        message = jwt
        if "Error" in jwt:
            status = False 
        else:

            fecha =  datetime.now()
            fecha_utc5 = fecha + timedelta(hours=-5)

            status = True
            message = json.loads(jwt)
            fecha_caducidad = message["expire_date"]
            if fecha_caducidad >= fecha_utc5.strftime("%Y-%m-%d %H:%M:%S"):
                status = True
            else:
                status = False
                message = "Token Expirado"

        return json.dumps({"status": status, "message": message})  
    except Exception as ex:
        print("Error jwt", ex)
        return json.dumps({"status": status, "message": ex})  
    
    
