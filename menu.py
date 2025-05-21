from productos import cargar_inventario

from productos import buscar_producto

from productos import ordenar_matriz

from productos import buscar_max_min

from productos import mostrar_precio_mayor

inventario = []

opcion = ""

opcion_salida = 0

while opcion != opcion_salida:
    print("-"*50)
    print("Sistema de inventario de “Empire Inventory” ")
    print ("1 - Cargar producto/s.") 
    print ("2 - Buscar producto.") 
    print ("3 - Ordenar inventario.") 
    print ("4 - Mostrar producto más caro y más barato") 
    print ("5 - Mostrar productos con precio mayor a 15000.")
    print ("0 - Salir")
    print("-"*50)

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        inventario = cargar_inventario()
    elif opcion == 2:
        buscar_producto(inventario)
    elif opcion == 3:
        ordenar_matriz(inventario)
    elif opcion == 4:
        buscar_max_min(inventario)
    elif opcion == 5:
        mostrar_precio_mayor(inventario)
    elif opcion == opcion_salida:
        print("Saliendo del programa.")
    else:
        print("Opcion incorrecta.")

