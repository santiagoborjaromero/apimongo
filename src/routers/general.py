import base64
from fastapi import APIRouter, Depends, Request
from src.models.hcommand_model import Hcommand
from src.models.general_model import DataRequest
from src.schemas.hcommand_schema import hcommandEntity, hcommandsEntity
from src.utils.functions import errorHandler, formatResponse, getTokenData, get_ws_origin, sendTokenData
from src.config.database import db
from datetime import datetime, timedelta
from ldap3 import Server, Connection, ALL,  SAFE_SYNC, AUTO_BIND_NO_TLS

router = APIRouter(tags=["General"])

@router.get("/getcmds", response_model=list[Hcommand], summary="Lista todos los comandos ejecutados en el servidor como historico")
async def data(origin: dict = Depends(get_ws_origin)): 
    try:
        token_data = getTokenData(origin)
        if (token_data["status"]):
            print("TOKEN OK")
            idcliente = token_data["message"]["idcliente"]
            print(idcliente)

            # newdata = await hcommandsEntity(db.hcommand.find({"idcliente": idcliente}))
            cursor = db.hcommand.find({"idcliente": idcliente})
            documents = await cursor.to_list(length=100)
            newdata = hcommandsEntity(documents)

            status = 1
            message = newdata
            # message = "asd"
        else:
            print("TOKEN FAKE")
            status = token_data["status"]
            message = token_data["message"]
            
    except Exception as err:
        status = 0
        message = errorHandler(err)
    return formatResponse(status, message)


@router.post("/savecmd", response_model=Hcommand, summary="Guarda los comandos y resultados ejecutados en el servidor del sentinel")
async def savecmd(request:Request, data: DataRequest,  origin: dict = Depends(get_ws_origin)): 
    try:
        token_data = getTokenData(origin)
        if (token_data["status"]):
            print("TOKEN OK")

            # document = data.model_dump()
            # print(document)

            document = dict(data)
            identificador = document["identificador"]
            data = document["data"]
            # print(document)
            # print(identificador)
            fecha =  datetime.now()
            fecha_utc5 = fecha + timedelta(hours=-5)
            # idn = ((base64.b64decode(document["identificador"])).decode(encoding="utf-8")).split("|")
            # data = document["data"] 
            inserciones = 0
            for d in data:
                
                cmd_string = d.cmd
                cmd_string_bytes = cmd_string.encode("ascii")
                base64_bytes = base64.b64encode(cmd_string_bytes)
                cmd = base64_bytes.decode("ascii")
                
                respuesta_string = d.respuesta
                respuesta_string_bytes = respuesta_string.encode("ascii")
                base64_bytes = base64.b64encode(respuesta_string_bytes)
                respuesta = base64_bytes.decode("ascii")
                
                hcmd = Hcommand(
                    idcliente = identificador.idcliente,
                    idservidor = identificador.idusuario,
                    idusuario = identificador.idservidor,
                    idoperacion = identificador.id,
                    idcola_comando = d.id,
                    fecha = fecha_utc5,
                    comando = cmd,
                    resultado = respuesta,
                )
                # print(hcmd)
                await db.historico_comandos.insert_one(dict(hcmd))
                inserciones +=1

            status = 1
            message = f"{inserciones} Registros adicionados"
        else:
            print("TOKEN FAKE")
            status = token_data["status"]
            message = token_data["message"]
    except Exception as ex:
        status = False
        print(ex)
        message = errorHandler(ex)

    return formatResponse(status, message)




@router.get("/ldap", response_model=list[Hcommand], summary="Lista todos los comandos ejecutados en el servidor como historico")
async def ldap(origin: dict = Depends(get_ws_origin)): 
    try:
        token_data = getTokenData(origin)
        token = sendTokenData(origin)

        # print(token_data)
        if (token_data["status"]):
            # print("TOKEN OK")
            # idcliente = token_data["message"]["idcliente"]
            # print(idcliente)

            # LDAP_SERVER_URL = "ldap://172.20.0.3"
            LDAP_SERVER_URL = "172.20.0.3"
            LDAP_PORT = 389
            # LDAP_BASE_DN = "dc=sercop,dc=com"  
            PASSWORD = "L1s4hUn14nd3s"
            USERNAME = "admin"

            # print(LDAP_SERVER_URL)

            server = Server(LDAP_SERVER_URL, port=LDAP_PORT, get_info=ALL)
            # conn = Connection(server, USERNAME, PASSWORD, client_strategy=SAFE_SYNC, auto_bind=AUTO_BIND_NO_TLS)
            conn = Connection(server, user= f'cn={USERNAME},dc=sercop,dc=com', password=PASSWORD, client_strategy=SAFE_SYNC, auto_bind=AUTO_BIND_NO_TLS)
            # status, result, response, _ = conn.search('cn=admin,dc=sercop,dc=com', '(objectclass=*)')  
            conn.start_tls()
            conn.bind()
            conn.search('dc=sercop,dc=com', '(uid=*)', attributes=['sn','cn', 'homeDirectory'], size_limit=0)
            for entrada in conn.response:
                print(entrada['dn'])
            # try:
            #     server = Server(LDAP_SERVER_URL, port=LDAP_PORT, get_info=ALL)
            #     conn = Connection(server, user=f"cn={USERNAME},{LDAP_BASE_DN}", password={PASSWORD})
            #     if conn.bind():
            #         conn.unbind()
            #         return True
            #     else:
            #         conn.unbind()
            #         return False
            # except Exception as e:
            #     print(f"LDAP authentication error: {e}")
            #     status = 0
            #     message = f"LDAP authentication error: {e}"

            status = 1
            message = []
            # message = "asd"
        else:
            print("TOKEN FAKE")
            status = token_data["status"]
            message = token_data["message"]
            
    except Exception as err:
        status = 0
        message = errorHandler(err)
    return formatResponse(status, message)

