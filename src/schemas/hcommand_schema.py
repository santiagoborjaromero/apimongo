def hcommandEntity(item) -> dict:
    return{
        "idcliente": item["idcliente"],
        "idservidor": item["idservidor"],
        "idusuario": item["idusuario"],
        "idagente": item["idusuario"],
        "idcola_comando": item["idcola_comando"],
        "fecha": item["fecha"],
        "comando": item["comando"],
        "resultado": item["resultado"],
    }


def hcommandsEntity(entity) -> list:
    return [hcommandEntity(item) for item in entity]