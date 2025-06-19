import base64
from fastapi import APIRouter, Depends
from src.models.hcommand_model import Hcommand
from src.models.general_model import DataRequest
from src.schemas.hcommand_schema import hcommandEntity, hcommandsEntity
from src.utils.functions import errorHandler, formatResponse, getTokenData, get_ws_origin
from src.config.database import db
from datetime import datetime

# $rec = [
#     "paq" => $obj->idcliente,
#     "ref" => $obj->idusuario,
#     "task" => $obj->idrol,
#     "expire_date" => date("Y-m-d H:i:s", strtotime('+1 day'))
# ];

router = APIRouter(tags=["General"])

@router.get("/getcmds", response_model=list[Hcommand], summary="Lista todos los comandos ejecutados en el servidor como historico")
async def data(origin: dict = Depends(get_ws_origin)): 
    try:
        token_data = getTokenData(origin)
        if (token_data["status"]):
            print("TOKEN OK")
            idcliente = token_data["message"]["paq"]
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


@router.post("/savecmd", response_model=Hcommand, summary="Salva los comandos y resultados ejecutados en el servidor")
async def data(data: DataRequest, origin: dict = Depends(get_ws_origin)): 
    try:
        token_data = getTokenData(origin)
        if (token_data["status"]):
            print("TOKEN OK")

            document = data.model_dump()

            idn = ((base64.b64decode(document["identificador"])).decode(encoding="utf-8")).split("|")
            data = document["data"] 

            inserciones = 0

            for d in data:
                hcmd = Hcommand(
                    idcliente = int(idn[0]),
                    idservidor = int(idn[1]),
                    idusuario = int(idn[2]),
                    idagente = int(idn[3]),
                    idcola_comando = int(d["id"]),
                    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    comando = d["cmd"],
                    resultado = d["respuesta"]
                )
                result = await db.hcommand.insert_one(dict(hcmd))
                inserciones +=1

            status = 1
            message = f"{inserciones} Registros adicionados"
        else:
            print("TOKEN FAKE")
            status = token_data["status"]
            message = token_data["message"]
    except Exception as ex:
        status = False
        message = errorHandler(ex)

    return formatResponse(status, message)