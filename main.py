#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mi Primera API FastAPI - Verificación de Setup
Desarrollador: [Fernanda Betancourt]
"""

from fastapi import FastAPI
import os
import sys
from datetime import datetime

# Crear instancia de FastAPI
app = FastAPI(
    title="Mi Primera API FastAPI",
    description="API de verificación para setup del bootcamp",
    version="1.0.0"
)

@app.get("/")
def home():
    """Endpoint principal de verificación"""
    return {
        "message": "¡Setup completado correctamente!",
        "project": "FastAPI Bootcamp - Semana 1",
        "timestamp": datetime.now().isoformat(),
        "status": "✅ Working perfectly"
    }

@app.get("/info/setup")
def info_setup():
    """Información del entorno de desarrollo"""
    return {
        "python_version": sys.version,
        "python_path": sys.executable,
        "working_directory": os.getcwd(),
        "virtual_env": os.environ.get("VIRTUAL_ENV", "No detectado"),
        "user": os.environ.get("USER", "No detectado"),
        "hostname": os.environ.get("HOSTNAME", "No detectado")
    }

@app.get("/health")
def health_check():
    """Endpoint de verificación de salud"""
    return {
        "status": "healthy",
        "message": "API running correctly",
        "environment": "development"
    }

@app.get("/info")
def info():
    return {"api": "FastAPI", "week": 1, "status": "running"}

@app.get("/greeting")
@app.get("/greeting/{name}")
def greet_user(name: str = "Fernanda"):
    return {"greeting": f"¡Hola {name}!"}

@app.get("/my-profile")
def my_profile():
    return {
        "name": "Fernanda",           # Cambiar por tu nombre
        "bootcamp": "FastAPI",
        "week": 1,
        "date": "2025",
        "likes_fastapi": True         # ¿Te gustó FastAPI?
    }