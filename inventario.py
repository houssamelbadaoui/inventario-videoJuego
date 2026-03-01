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
    
    # metodo para usar un objeto
    def usarObjeto(self, nombre, elemento=None):
        for objeto in self.objetos:
            # encontrar el objeto que lo queremos a usar
            if objeto["nombre"] == nombre:

                if elemento is not None and objeto["elemento"] != elemento:
                    continue

                if objeto["usos"] > 1:
                    objeto["usos"] -= 1
                else:
                    self.objetos.remove(objeto)
                return True
        return False