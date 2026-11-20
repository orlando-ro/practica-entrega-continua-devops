# Práctica DevOps - Hola Mundo (Python + Docker)

Aplicación web sencilla en Python usando Flask, empaquetada con Docker.

## Archivos

- `app.py`: Servidor web Flask con rutas `/` y `/health`.
- `requirements.txt`: Dependencias de Python (`flask==3.1.0`).
- `Dockerfile`: Definición de la imagen basada en `python:3.11-slim`.
- `.dockerignore`: Exclusiones para el contexto de construcción de Docker.

## Uso local con Docker

### 1. Construir la imagen
```bash
docker build -t hola-mundo-python:latest .
```

### 2. Ejecutar el contenedor
```bash
docker run -d -p 5000:5000 --name hola-mundo hola-mundo-python:latest
```
Abrir en el navegador: `http://localhost:5000`

### 3. Subir a Docker Hub
```bash
docker login
docker tag hola-mundo-python:latest <tu-usuario>/hola-mundo-python:latest
docker push <tu-usuario>/hola-mundo-python:latest
```
La URL de la imagen quedará en:
`https://hub.docker.com/r/<tu-usuario>/hola-mundo-python`
