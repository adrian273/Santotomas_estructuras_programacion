"""fruit_store.py
    @description: Leer archivo JSON
"""

import json
import os.path


#  Encontrar el directorio donde se encuentra el script
path = os.path.dirname(__file__)
#  os.path.join(path1[, path2[, …]]) → Une dos o más 
# componentes de una ruta de forma inteligente
fruit_store = os.path.join(path, 'data/fruit_store_data.json')

with open(fruit_store) as data_file:
    data = json.load(data_file)

print(data['Fruteria'])