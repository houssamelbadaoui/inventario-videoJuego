import json
class ObjetoInventario:

    # Los datos leídos desde el JSON deberán transformarse en objetos de esta clase 
    # antes de almacenarse en el inventario.
    def __init__(self, nombre, categoria, contenedor, usos, elemento, energia):
        self.nombre = nombre
        self.categoria = categoria
        self.contenedor = contenedor
        self.usos = usos
        self.elemento = elemento
        self.energia = energia




class InventarioJugador:

    # constructor
    def __init__(self, archivo):
        # leer el archivo.json
        with open(archivo, "r", encoding="utf-8") as file:
            # guardar lo en una lista
            datos = json.load(file)

            self.objetos = []

            for item in datos:
                objeto = ObjetoInventario(
                    item["nombre"],
                    item["categoria"],
                    item["contenedor"],
                    item["usos"],
                    item["elemento"],
                    item["energia"]
                )
                self.objetos.append(objeto)

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
        
    # metodo estrategia sobre carga, que devuelve la cat que tiene 
    # mas energia * usos
    def estrategiaSobreCarga(self):

        # Dicc para almacenar la energia total acumulada por cat
        energia_por_categoria = {}

        for objeto in self.objetos:
            categoria = objeto["categoria"]
            # calcular energia total de cada objeto
            energia_total = objeto["usos"] * objeto["energia"]

            # añadimos las cat al dicc y inicia con 0
            if categoria not in energia_por_categoria:
                energia_por_categoria[categoria] = 0

            energia_por_categoria[categoria] += energia_total

        # si el invintario esta vacio, devolvemos lista vacia
        if not energia_por_categoria:
            return []
        
        # encontramos la cat con mayor energia total
        categoria_max = max(energia_por_categoria, key=energia_por_categoria.get)

        # devolver todos los obj que pertenezcan a la cat con mayor energia total
        return [obj for obj in self.objetos if obj["categoria"] == categoria_max]