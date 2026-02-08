## Comandos necesarios para correr el proyecto

### Iniciar el proyecto
```bash
docker-compose up --build
# o simplemente
docker-compose up
```

### Acceder al contenedor
```bash
docker exec -it core /bin/bash
```

### Comandos útiles
```bash
# Remover las imágenes
docker-compose down

# Construir desde cero sin caché
docker-compose build --no-cache

# Iniciar después de reconstruir
docker-compose up
```

SECRET_KEY="django-insecure-b1!i9)i!k0kw1vp!^e(bar71q7(!41z&m4r1$((9f&j(ztwd%^"

ALLOWED_HOSTS = *

DATABASES_NAME="django_db"
DATABASES_USER="django"
DATABASES_PASSWORD="postgres"
DATABASES_HOST="postgresql"
DATABASES_PORT="5432"

REDIS_URL="redis://django-redis:6379"