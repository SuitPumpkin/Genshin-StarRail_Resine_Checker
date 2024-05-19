import subprocess
import sys
from importlib.metadata import version, PackageNotFoundError
import os

# Lista de dependencias
dependencies = [
    'qasync',
    'asyncqt',
    'pyqt5',
    'genshin',
    'genshinstats',
    'qrcode',
    'aiohttp',
    'pydantic',
    'rsa'
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Comprobar e instalar las dependencias
for package in dependencies:
    try:
        # Verificar si el paquete está instalado y obtener su versión
        installed_version = version(package)
        print(f"{package} está instalado (versión {installed_version}).")
    except PackageNotFoundError:
        # El paquete no está instalado
        print(f"{package} no está instalado. Instalando...")
        install(package)
