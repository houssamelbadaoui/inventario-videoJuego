import json
class InventarioJugador:

    # constructor
    def __init__(self, archivo):
        # leer el archivo.json
        with open(archivo, "r", encoding="utf-8") as file:
            # guardar lo en una lista
            self.objetos = json.load(file)

    
