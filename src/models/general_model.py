from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, PydanticUserError
try:
    
    class DataItem(BaseModel):
        id: int
        cmd: str
        respuesta: str

    class DataRequest(BaseModel):
        identificador: str
        data: List[DataItem]

    model_config = {"from_attributes": True}

except PydanticUserError as exc_info:
    assert exc_info.code == 'schema-for-unknown-type'

