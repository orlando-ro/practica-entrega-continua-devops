# Práctica DevOps - Hola Mundo (Python + Docker)

Aplicación web sencilla en Python usando Flask, empaquetada con Docker.

## Archivos

- `app.py`: Servidor web Flask con rutas `/` y `/health`.
- `requirements.txt`: Dependencias de Python (`flask==3.1.0`).
- `Dockerfile`: Definición de la imagen basada en `python:3.11-slim`.
- `.dockerignore`: Exclusiones para el contexto de construcción de Docker.
