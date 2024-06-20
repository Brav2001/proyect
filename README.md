# Nombre del Proyecto

## Descripción

Prueba CRUD TMsoft.

#Configuración del Proyecto

## Base de Datos

La configuración por defecto de la base de datos es la siguiente:

```
Nombre de la base de datos: tmsoft
URL: localhost
Puerto: 3306
Usuario: root
```

Puedes cambiar la configuración de la base de datos editando el archivo .env.

## Ejemplo de configuración en .env:

```
DATABASE_URL=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_NAME=tmsoft
DATABASE_PASSWORD=

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1600
```

## Instalación de Dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```
pip install -r requirements.txt
```

### Creación de Usuario por Defecto

El proyecto crea automáticamente un usuario por defecto con las siguientes credenciales:

```
Documento: 111111111
Contraseña: password
```

# Ejecución del Proyecto

## Backend (API)

Para ejecutar el backend, asegúrate de haber configurado la base de datos y haber instalado las dependencias como se mencionó anteriormente. Luego, ejecuta el siguiente comando:

```
python -m uvicorn app:app --reload
```

## Frontend

Para el frontend, sigue estos pasos:

Instala las dependencias con npm:

```
npm install

npm run dev
```

Configuración de la URL de la API en el Frontend
Puedes cambiar la URL de la API editando el archivo src/api.js si es necesario.
