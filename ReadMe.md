Tutorial Django Endpoints (DRF + Swagger + API Key)

Descripcion del proyecto
Este repo es un tutorial para aprender a construir endpoints con Django REST Framework. Incluye:
- DRF: framework para crear APIs en Django con serializers, viewsets y el Browsable API.
- OpenAPI/Swagger: especificacion y UI para documentar y probar los endpoints (drf-spectacular).
- Endpoints para usuarios y perfiles (UserProfile).
- Seguridad con API key y opcion de login para el Browsable API.

UIs disponibles
- DRF Browsable API: `http://127.0.0.1:8000/api/`
- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- Redoc: `http://127.0.0.1:8000/api/redoc/`

Pasos de instalacion (desde este repo)
1) Crear entorno virtual
```bash
python -m venv .venv
source .venv/bin/activate #mac
.\venv\Scripts\activate #windows

```

2) Instalar dependencias
```bash
pip install -r requirements.txt
```

3) Migraciones
```bash

cd api # Ir a ruta api
python manage.py makemigrations
python manage.py migrate
```

4) Crear superusuario (opcional, para admin)
```bash
python manage.py createsuperuser
```

5) Crear un API key
```bash
python manage.py shell
```
```python
from rest_framework_api_key.models import APIKey
api_key, key = APIKey.objects.create_key(name="local-dev")
print(key)
```

6) Ejecutar servidor
```bash
python manage.py runserver
```

Si empiezas de cero (crear proyecto y app)
```bash
django-admin startproject config api
python manage.py startapp users
```

Pasos del tutorial
1) Configurar settings en `api/config/settings.py`.
2) Crear el modelo `UserProfile` en `api/users/models.py`.
3) Crear serializers en `api/users/serializers.py`.
4) Configurar permisos en `api/users/permissions.py`.
5) Crear viewsets en `api/users/views.py`.
6) Crear rutas del app en `api/users/urls.py`.
7) Configurar rutas globales y Swagger en `api/config/urls.py`.

Notas importantes al probar endpoints
- El header correcto es `Authorization: Api-Key <tu_key>` (si olvidas el prefijo, da 403).
- El API key se guarda en la base de datos, no en settings.
- Swagger requiere Authorize para enviar el API key.
- Si haces login en el Browsable API, las llamadas usan cookie de sesion.
- Si no aparece el boton Authorize, revisa `SPECTACULAR_SETTINGS` y recarga la pagina.

Uso de `api.http` con la extension Rest Client
1) Instala la extension "REST Client" en VS Code (autor: Huachao Mao).
2) Abre el archivo `api.http`.
3) Escribe una peticion en este formato:
```
GET http://127.0.0.1:8000/api/users/
Authorization: Api-Key <tu_key>
Accept: application/json
```
4) Haz clic en "Send Request" (aparece arriba de la linea de la peticion).
5) Veras la respuesta en un panel a la derecha.

Ejemplo para crear un perfil:
```
POST http://127.0.0.1:8000/api/profiles/
Authorization: Api-Key <tu_key>
Content-Type: application/json

{
  "user_id": 1,
  "bio": "Hola!",
}
```
