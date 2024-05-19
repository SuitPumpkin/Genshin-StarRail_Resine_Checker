import subprocess

# Comprobar e instalar dependencias en caso de no tenerlas
subprocess.run(["python", "Dependencies.py"],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# Ejecutar el programa
subprocess.run(["python", "App.py"])
