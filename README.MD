# Api - Mongo
### [FastAPI](https://fastapi.tiangolo.com/)

**Inicio:** 2025-06-18

## Instalación
![](https://img.shields.io/badge/Python-3.12-blue) 
![](https://img.shields.io/badge/Framework-FastAPI-gr) 
![](https://img.shields.io/badge/Base_de_Datos-MongoDB-red) 


Crear entoerno virtual
```bash
# Entorno virtual
python -m venv venv
.\venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

Para correr el servidor
```bash
uvicorn main:app --port 5000 --reload    
uvicorn main:app --host 0.0.0.0 --port 5000
```

Ahora se puede modificar creando un mejor servidor o codigo tomando como referencia la pagina oficial de soporte de [UVICON](https://www.uvicorn.org/).


## Importante
Para ver la documentacion de las rutas se puede poner el siguiente link en el browser
```bash
http://127.0.0.1:5000/redoc
http://127.0.0.1:5000/docs
```

# Docker

Build
```
docker build -t lisah-api-mongo .
```

Correr el Doclker
```
docker run -it -p 5000:5000 lisah-api-mongo
```