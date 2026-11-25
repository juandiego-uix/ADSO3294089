CLONAR EL REPOSITORIO

git clone https://github.com/juandiego-uix/ADSO3294089.git

cd ADSO4089

CREA EL ENTORNO VIRTUAL

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

COMPLETA LOS CREDENCIALES DE .env

CONFIGURA CORS PARA FLUTTER WEB

La API permite por defecto aplicaciones servidas desde http://localhost y
http://127.0.0.1, con cualquier puerto. Si la aplicación web se sirve desde
otro dominio o desde la IP de otro equipo, agrega ese origen en la variable
de entorno CORS_ORIGINS del servicio de Render. Usa el origen exacto, sin ruta;
separa varios orígenes con comas. Por ejemplo:

CORS_ORIGINS=https://mi-frontend.example.com,http://192.168.1.20:5000

Después de guardar la variable, reinicia o vuelve a desplegar la API. No uses
* como origen en producción. CORS aplica a Flutter Web; las aplicaciones
nativas de Android no están sujetas a esta restricción del navegador.

ELIMINAR PERSONAS

La ruta DELETE /personas/<per_uuid> elimina personas sin registros asociados.
Si la persona tiene aprendices, instructores o matrículas relacionados, la API
responde HTTP 409 e indica cuáles deben resolverse antes de borrar la persona.

DESPLIEGUE DE LA API EN RENDER

La API se publica como un Web Service conectado a este repositorio y a la rama
main. Configura el servicio con:

- Build Command: pip install -r requirements.txt
- Start Command: gunicorn --bind 0.0.0.0:$PORT app:app
- Health Check Path: /

En Environment agrega las variables MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD,
MYSQL_DB y MYSQL_PORT con los datos de la base de datos cloud que ya utiliza
el proyecto. MYSQL_SSL_CA usa ca.pem por defecto. No guardes credenciales en
GitHub ni en este archivo.

El origen web de Render ya está permitido en CORS:
https://adso4089-mobile-web-juangamers.onrender.com. Si publicas el frontend
con otro dominio, agrégalo en la variable CORS_ORIGINS del Web Service, sin
ruta y separado por comas si hay varios dominios. La variable también permite
conservar el acceso desde localhost y 127.0.0.1 durante desarrollo.


INICIAR

python app.py


