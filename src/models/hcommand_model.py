from typing import Optional
from datetime import datetime
from pydantic import BaseModel, PydanticUserError
try:
    class Hcommand(BaseModel):
        idcliente: int | None = None
        idservidor: int | None = None
        idusuario: int | None = None
        idagente: int | None = None
        idcola_comando: int | None = None
        fecha: str | None = None
        resultado: str | None = None

    model_config = {"from_attributes": True}

except PydanticUserError as exc_info:
    assert exc_info.code == 'schema-for-unknown-type'

