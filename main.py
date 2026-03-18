from inventario import InventarioJugador

if __name__ == "__main__":

    # creamos una instancia del inventario
    # leyendo los datos desde el archivo JSON
    inventario = InventarioJugador("inventario.json")


    # prueba 1: Buscar objetos por energia maxima
    print("Buscar objetos con energia <= 10")
    print(inventario.buscarPorEnergia(10))

    # prueba 2: Usar un objeto
    print("Usar 'Pocion pequeña'")
    print(inventario.usarObjeto("Bomba eléctrica", elemento="electricidad"))

    # prueba 3: Consultar Usos disponibles
    print("Consultar usos de categoria 'recuperacion'")
    print("Total de usos disponibles: ", inventario.consultarUsos(nombre="armento", categoria="recuperacion", elemento="recupercaion"))

    # prueba 4: estrategia de sobrecarga

    print("Objetos de la categoria con mas energia total: ")
    print(inventario.estrategiaSobreCarga())
