#!/bin/bash

# validar que se pase un argumento (nombre del archivo)
if [ -z "$1" ]; then
 echo "por favor proporcionar el nombre del archivo. "
 exit 1
fi 

# Permitir la ejecucion del archivo
chmod +x $1

# Cambiar la propiedad del archivo root
sudo chown root:root $1 

echo "Se han modificado los permisos y la propiedad del archivo '$1'." 
