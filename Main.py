import subprocess

# Comprobar e instalar dependencias en caso de no tenerlas
subprocess.run(["python", "Dependencies.py"])
# Ejecutar el programa
subprocess.run(["python", "App.py"])
