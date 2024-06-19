# My Movie Collection API

## Descripción

Esta API permite gestionar una colección de películas, incluyendo la creación, lectura, actualización y eliminación de registros de películas.

## Instalación

### Requisitos

- Docker
- Docker Compose (opcional)

### Configuración

1. Clona este repositorio.
2. Crea un archivo `.env` en el directorio raíz y añade las variables de entorno necesarias.

### Uso

#### Con Docker

1. Construye la imagen de Docker:
    ```bash
    docker build -t movie-collection-api .
    ```
2. Ejecuta el contenedor:
    ```bash
    docker run -p 5000:5000 movie-collection-api
    ```

#### Sin Docker

1. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
2. Ejecuta la aplicación:
    ```bash
    flask run
    ```

## Endpoints

- `GET /movies`: Obtiene todas las películas.
- `GET /movies/<id>`: Obtiene una película por su ID.
- `POST /movies`: Crea una nueva película.
- `PUT /movies/<id>`: Actualiza una película por su ID.
- `DELETE /movies/<id>`: Elimina una película por su ID.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para discutir los cambios que te gustaría hacer.
