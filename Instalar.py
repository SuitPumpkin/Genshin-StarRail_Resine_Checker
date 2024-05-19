import subprocess
import sys

# Lista de dependencias
dependencies = [
    'genshin',
    'genshinstats',
    'qrcode',
    'aiohttp',
    'pydantic',
    'rsa'
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Comprobar e instalar las dependencias
for package in dependencies:
    try:
        __import__(package)
    except ImportError:
        print(f"Instalando {package}...")
        install(package)

# Tu código principal aquí
print("Todas las dependencias han sido instaladas.")
