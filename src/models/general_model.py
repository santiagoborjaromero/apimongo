from typing import List
from pydantic import BaseModel, PydanticUserError
try:
    
    class DataItem(BaseModel):
        id: str
        cmd: str
        respuesta: str

    class DataIdentificador(BaseModel):
        id: int
        idcliente: int
        idusuario: int
        idservidor: int

    class DataRequest(BaseModel):
        action: str
        identificador: DataIdentificador
        data: List[DataItem]

    model_config = {"from_attributes": True}

except PydanticUserError as exc_info:
    assert exc_info.code == 'schema-for-unknown-type'

