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
