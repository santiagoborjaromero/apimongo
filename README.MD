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
fastapi dev main.py --port 5000
```

Ahora se puede modificar creando un mejor servidor o codigo tomando como referencia la pagina oficial de soporte de [UVICON](https://www.uvicorn.org/).


## Importante
Para ver la documentacion de las rutas se puede poner el siguiente link en el browser
```bash
http://127.0.0.1:5000/redoc
http://127.0.0.1:5000/docs
```
Para unir redes de docker
```bash
#Listar redes
docker network ls

#Crear redes
docker network create mired


docker network connect {red} {contenedor}

Ej:
docker network connect mired nice_hoover  
```
Para saber la ip de cada contenedor
```bash
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nice_hoover
```


```bash
ldapadd -x -w L1s4hUn14nd3s -D "cn=admin,dc=sercop,dc=com" << EOF
# LDIF file to add organizational unit "ou=devops" under "dc=sercop,dc=com"
dn: ou=devops,dc=sercop,dc=com
objectClass: organizationalUnit
ou: devops

# LDIF file to add organizational unit "ou=appdev" under "dc=sercop,dc=com"
dn: ou=appdev,dc=sercop,dc=com
objectClass: organizationalUnit
ou: appdev
EOF

# USUARIOS

ldapadd -x -w L1s4hUn14nd3s -D "cn=admin,dc=sercop,dc=com" << EOF
# LDIF file to Create user "santiago.borja" in "ou=appdev" under "dc=sercop,dc=com"
dn: cn=amrutha,ou=devops,dc=sercop,dc=com
objectClass: person
cn: santiago.borja
sn: Santiuago Borja
userPassword: L1s4hUn14nd3s

# LDIF file to Create user "hugo.herrera" in "ou=appdev" under "dc=sercop,dc=com"
dn: cn=charlie,ou=appdev,dc=sercop,dc=com
objectClass: inetOrgPerson
cn: hugo.herrera
sn: Hugo Herrera
userPassword: L1s4hUn14nd3s

# LDIF file to Create user "jorge.lopez" in "ou=appdev" under "dc=sercop,dc=com"
dn: cn=amit,ou=appdev,dc=sercop,dc=com
objectClass: inetOrgPerson
cn: jorge.lopez
sn: Jorge Lopez
userPassword: L1s4hUn14nd3s
EOF


ldapsearch -x -b dc=sercop,dc=com -D "cn=admin,dc=sercop,dc=com" -w L1s4hUn14nd3s -s sub "objectclass=*"

```



