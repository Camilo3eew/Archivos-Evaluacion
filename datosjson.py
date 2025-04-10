import json
from datetime import datetime

# Abrir el archivo JSON y cargarlo usando json.load
with open('myfile.json') as archivo:
    ourjson = json.load(archivo)

# Asignar el contenido a la variable json_file
json_file = ourjson

# Obtener el token desde el archivo JSON
token = json_file.get("token")

# Obtener la fecha de expiración y calcular el tiempo restante
expiracion_str = json_file.get("expiracion")
expiracion = datetime.strptime(expiracion_str, "%Y-%m-%d %H:%M:%S")
ahora = datetime.now()
tiempo_restante = expiracion - ahora

# Imprimir los resultados
print(f"Token: {token}")
print(f"Tiempo restante antes de la expiración: {tiempo_restante}")

