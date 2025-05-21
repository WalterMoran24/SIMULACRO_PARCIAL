inventario = []


def cargar_inventario():
    '''Mediante un input ingresa la cantidad de productos a ingresar, luego mediante un
    bucle for y utilizando el metodo "range" se recorre la cantidad de productos.'''

    cantidad_productos = int(input("Ingrese la cantidad de productos a registrar: "))

    inventario = [["", 0.0, 0] for _ in range(cantidad_productos)]  
    
    
    for i in range(cantidad_productos):
        print(f"Producto {i+1}:")
        inventario[i][0] = input("Nombre del producto: ")
        inventario[i][1] = float(input("Precio del producto: "))
        inventario[i][2] = int(input("Cantidad del producto: "))

    return inventario


def buscar_producto(inventario):
    '''Verifica si la matriz está vacía,de sera si, arrojara un mensaje y finalizara.
    De lo contrario, permitira buscar un producto mediante su nombre, en caso de no
    existir, arrojara un mensaje de que no se encuentra en stock'''
    if not inventario: 
        print("No hay productos registrados en el inventario.")
        return
    
    busqueda = input("Ingrese el nombre del producto que quiere buscar: ")
    
    encontrado = False
    
    for producto in inventario:
        if producto[0] == busqueda: 
            print(f"Producto encontrado:\nNombre: {producto[0]}\nPrecio: ${producto[1]}\nCantidad: {producto[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print("\nEl producto no está en el inventario.")


########################################################################################################################

def ordenar_matriz(inventario):
    '''Permite ordenar de manera ascendente la matriz segun su precio'''
    if not inventario:
        print("No hay productos registrados en el inventario.")
        return
    
    n = len(inventario)
    for i in range(n):
        for j in range(0, n-i-1):
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]

    print("\nInventario ordenado por precio (ascendente):")
    for producto in inventario:
        print(f"Nombre: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}")


def buscar_max_min(inventario):
    '''Permmite buscar el valor maximo y minimo de todos los valores que se encuentren
    en la matriz siempre y cuando, no este vacia'''
    if not inventario:
        print("No hay productos registrados en el inventario.")
        return
    
    mas_caro = inventario[0]
    mas_barato = inventario[0]
    
    for producto in inventario:
        if producto[1] > mas_caro[1]:
            mas_caro = producto
        if producto[1] < mas_barato[1]:
            mas_barato = producto
    
    print(f"\nProducto más caro:\nNombre: {mas_caro[0]}\nPrecio: ${mas_caro[1]:.2f}\nCantidad: {mas_caro[2]}")
    print(f"\nProducto más barato:\nNombre: {mas_barato[0]}\nPrecio: ${mas_barato[1]:.2f}\nCantidad: {mas_barato[2]}")



########################################################################################################################


def mostrar_precio_mayor(inventario):
    '''mediante comprension de listas verifica que productos superan el valor de 15000'''
    if not inventario:
        print("No hay productos registrados en el inventario.")
        return
    
    productos_caros = [producto for producto in inventario if producto[1] > 15000]
    
    if productos_caros:
        print("\nProductos con precio mayor a $15,000:")
        for producto in productos_caros:
            print(f"Nombre: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}")
    else:
        print("\nNo hay productos con precio mayor a $15,000.")


########################################################################################################################


