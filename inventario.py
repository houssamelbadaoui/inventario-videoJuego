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
                # if the user specify an element we should find it
                if elemento is not None and objeto["elemento"] != elemento:
                    continue

                if objeto["usos"] > 1:
                    objeto["usos"] -= 1
                else:
                    self.objetos.remove(objeto)
                return True
        return False
    
    # metodo para consultar usos de un elemento, categoria, o objeto especifico
    def consultarUsos(self, nombre=None, categoria=None, elemento=None):

        total_usos = 0

        for objeto in self.objetos:
             
             if nombre is not None and objeto["nombre"] != nombre:
                 continue
             
             if categoria is not None and objeto["categoria"] != categoria:
                 continue
             
             if elemento is not None and objeto["elemento"] != elemento:
                 continue
             total_usos += objeto["usos"]

             return total_usos