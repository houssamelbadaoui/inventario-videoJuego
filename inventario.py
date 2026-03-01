import json
class InventarioJugador:

    # constructor
    def __init__(self, archivo):
        # leer el archivo.json
        with open(archivo, "r", encoding="utf-8") as file:
            # guardar lo en una lista
            self.objetos = json.load(file)

    # buscarPorEnergia, buscar objetos cuya energia por uso sea menor o igual
    # al numero dado
    def buscarPorEnergia(self, max_energia):
        resultados = []

        for objeto in self.objetos:
            if objeto["energia"] <= max_energia:
                resultados.append(objeto)
        return resultados
