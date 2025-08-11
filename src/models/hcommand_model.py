from datetime import datetime
from pydantic import BaseModel, PydanticUserError
try:
    class Hcommand(BaseModel):
        idcliente: int | None = None
        idservidor: int | None = None
        idusuario: int | None = None
        idoperacion: int | None = None
        idcola_comando: str | None = ""
        fecha: datetime | None = None
        comando: str | None = None
        resultado: str | None = None

    model_config = {"from_attributes": True}

except PydanticUserError as exc_info:
    assert exc_info.code == 'schema-for-unknown-type'

