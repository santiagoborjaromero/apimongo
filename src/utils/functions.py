from fastapi.responses import JSONResponse

from fastapi import Depends, HTTPException, Request, Security
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials, HTTPBearer
from jwt import encode, decode
from jwt import exceptions
from datetime import date, datetime, timedelta
from fastapi.responses import JSONResponse
from bson import json_util
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
    # return JSONResponse({"status": status, "message": object})


def get_ws_origin(api_key: str = Security(APIKeyHeader(name='Authorization'))):
    return api_key

def getTokenData(api_key:str):
    tokenOriginal = api_key.split(" ")[1]
    dToken = json_util.loads(validate_token(tokenOriginal))
    return dToken

# $rec = [
#     "paq" => $obj->idcliente,
#     "ref" => $obj->idusuario,
#     "task" => $obj->idrol,
#     "expire_date" => date("Y-m-d H:i:s", strtotime('+1 day'))
# ];
# {'status': True, 'data': '{"ref":6,"paq":1,"task":4,"expire_date":"2025-06-19 22:41:07"}'}

def validate_token(token):
    jwt = ""
    try:
        jwt = decrypt(token)
        # print(jwt)
        message = jwt
        if "Error" in jwt:
            status = False 
        else:
            status = True
            message = json_util.loads(jwt)
            fecha_caducidad = message["expire_date"]
            if fecha_caducidad >= datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
                status = True
            else:
                status = False
                message = "Token Expirado"

        return json_util.dumps({"status": status, "message": message})  
    except Exception as ex:
        print("Error jwt", ex)
        return json_util.dumps({"status": status, "message": ex})  
    
    
