# PT-Webtools

PT-WebTools es una aplicación Django diseñada para manejar encuestas y respuestas, con autenticación basada en tokens y soporte para Docker.

- Tiempo dedicado: 4 horas aproximadamente.
- Algunas decisiones tomadas: Elección de Django REST Framework ya que es una herramienta robusta para contruir una API ya que permite manejar serialización, vistas, autenticación, etc. Se ha cambio la ubicación de los tests dentro de la carpeta app porque están relacionados con la aplicación en específica (mejor organización, facilidad de ejecución y separación de lógica). Elección de SQLite como base de datos por defecto, pero si se planeara desplegar en producción sería más recomendable migrar a una más robusta como PostgreSQL.
- Bonus realizados: autenticación, docker, gestión de usuario con administración de django.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

- Python 3.9 o superior
- Docker (opcional, para ejecutar el proyecto en contenedores)
- Django y Django REST Framework
- Postman (opcional, para probar la API)

---

## Configuración inicial

### 1. Crear un entorno virtual
Crea y activa un entorno virtual para instalar las dependencias del proyecto:

```bash
python -m venv env
source env/bin/activate  # En macOS/Linux
env\Scripts\activate     # En Windows
```

### 2. Instalar dependencias
Instala las dependencias del proyecto desde el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. Configuración
Puedes cambiar la configuración de la base de datos en settings.py si lo necesitas.

Aplica las migraciones para configurar la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crea un superusuario
Crea un superusuario para acceder al panel de administración de Django:
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para ingresar un nombre de usuario, correo electrónico y contraseña.

---

## Uso de la API
1. Obtener un token de autenticación
La aplicación utiliza autenticación basada en tokens. Para obtener un token:

- Accede a la URL: http://localhost:8000/api-token-auth/
- Envía una solicitud POST con las credenciales del usuario:
    ```bash
    Key: username, Value: tu_usuario
    Key: password, Value: tu_contraseña
    ```
Ejemplo de respuesta:
```bash
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

2. Usar el token en las solicitudes
Incluye el token en el encabezado de tus solicitudes para autenticarte:
```bash
Key: Authorization
Value: Token <tu_token>
```

Ejemplo de solicitud GET a la API:
```bash
curl -X GET http://localhost:8000/api/responses/ \
-H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

---

## Uso de la API
1. Ejecutar el servidor de desarrollo
Para iniciar el servidor de desarrollo de Django:
```bash
python [manage.py](http://_vscodecontentref_/5) runserver
```

Accede a la aplicación en tu navegador en http://127.0.0.1:8000.

---

## Pruebas
Para ejecutar los tests del proyecto, usa el siguiente comando:
```bash
python manage.py test app
```

---

## Uso con Docker
1. Construir la imagen Docker
Construye la imagen Docker del proyecto:
```bash
docker build -t pt-webtools .
```

2. Ejecutar el contenedor
Ejecuta el contenedor Docker:
```bash
docker run -p 8000:8000 pt-webtools
```
Esto iniciará la aplicación en el contenedor. Accede a ella desde http://127.0.0.1:8000.

---

## Endpoints principales
1. Listar respuestas
```bash
URL: /api/responses/
Método: GET
Autenticación: Requerida
```
2. Crear una respuesta
```bash
URL: /api/responses/
Método: POST
Autenticación: Requerida
```
Cuerpo de la solicitud:
```bash
{
  "data": {
    "pregunta_1": "Respuesta A",
    "pregunta_2": "Respuesta B"
  },
  "contact_email": "usuario@example.com"
}
```

3. Detalle de una respuesta
URL: /api/responses/<id>/
Método: GET
Autenticación: Requerida