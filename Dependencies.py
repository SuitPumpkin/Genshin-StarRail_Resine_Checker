import subprocess
import sys
import pkg_resources

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
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Comprobar e instalar las dependencias
for package in dependencies:
    try:
        # Verificar si el paquete está instalado
        pkg_resources.get_distribution(package)
        print(f"{package} ya está instalado.")
    except pkg_resources.DistributionNotFound:
        # El paquete no está instalado
        print(f"Instalando {package}...")
        install(package)
    except pkg_resources.VersionConflict:
        # El paquete está instalado pero no está actualizado
        print(f"Actualizando {package}...")
        install(package)

print("Todas las dependencias han sido instaladas y/o actualizadas.")
