# Importar funciones desde archivos externos y la librería sys para salir del programa
from funciones_vista import *  # Importa funciones relacionadas con la vista (interfaz del usuario)
from funciones_database import *  # Importa funciones para interactuar con la base de datos
import sys  # Se utiliza para salir del programa

# Función principal para gestionar el flujo del programa
def iniciar_programa():
    """
    Crea la base de datos si no existe.
    Muestra el menú principal en un bucle infinito y procesa la opción seleccionada por el usuario.
    """
    db_crear_tabla_productos()
    while True:
        mostrar_menu()  # Muestra las opciones del menú
        opcion = input("Seleccione una opción: ")  # Captura la opción ingresada por el usuario
        procesar_opcion_menu(opcion)  # Procesa la opción seleccionada

# Función que procesa las opciones seleccionadas en el menú
def procesar_opcion_menu(opcion):
    """
    Recibe la opción seleccionada por el usuario y llama a la función correspondiente.
    """
    if opcion == '1':
        opcion_procesar_producto()  # Agregar un nuevo producto
    elif opcion == '2':
        opcion_visualizar_productos()  # Mostrar todos los productos
    elif opcion == '3':
        opcion_actualizar_producto()  # Actualizar un producto existente
    elif opcion == '4':
        opcion_eliminar_producto()  # Eliminar un producto
    elif opcion == '5':
        opcion_buscar_producto()  # Buscar un producto por ID
    elif opcion == '6':
        opcion_reporte_bajo_stock()  # Generar un reporte de productos con bajo stock
    elif opcion == '7':
        print("Saliendo del programa...")
        sys.exit()  # Termina la ejecución del programa
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")  # Mensaje de error para opciones inválidas

# Función para registrar un nuevo producto
def opcion_procesar_producto():
    """
    Solicita al usuario los datos de un producto, los registra en la base de datos y muestra un mensaje de confirmación.
    La lectura de datos está validad según el tipo de dato.
    """    
    nombre = leerString("Ingrese el nombre del producto: ")
    descripcion = leerString("Ingrese una descripción del producto: ")
    cantidad = leerInt("Ingrese la cantidad en stock: ")
    precio = leerFloat("Ingrese el precio del producto: ")
    categoria = leerString("Ingrese la categoría del producto: ")

    resultado = registrar_producto(nombre, descripcion, cantidad, precio, categoria)  # Guarda el producto en la base de datos

    if resultado:
        mostrar_mensaje_subrayado("Producto guardado con éxito")  # Confirmación de éxito
    else:
        mostrar_mensaje_subrayado("Se produjo un error al guardar el producto", Fore.RED)  # Mensaje de error

# Función para visualizar los productos
def opcion_visualizar_productos():
    """
    Recupera y muestra una lista de todos los productos del inventario.
    """
    inventario = todos_productos()  # Obtiene todos los productos de la base de datos

    if inventario:
        mostrar_mensaje_subrayado("------ Lista de Productos ------")
        for indice, producto in enumerate(inventario, 1):  # Enumera y muestra los productos
            imprimir_producto(producto)
    else:
        mostrar_mensaje_subrayado("No hay productos en el inventario.", Fore.RED)  # Mensaje si no hay productos

# Función para actualizar un producto existente
def opcion_actualizar_producto():
    """
    Solicita el ID de un producto, permite actualizar su cantidad y precio, y guarda los cambios.
    """
    id = leerInt("Ingrese el ID del producto que desea actualizar: ")
    
    producto = obtener_productos_por_id(id)  # Busca el producto por ID
    if producto:
        imprimir_producto(producto)  # Muestra la información actual del producto
        
        # Solicita los nuevos datos del producto
        nueva_cantidad = leerInt("Ingrese la nueva cantidad: ")
        nuevo_precio = leerFloat("Ingrese el nuevo precio: ")
        
        resultado = actualizar_producto(id, nueva_cantidad, nuevo_precio)  # Actualiza el producto en la base de datos
        
        if resultado:
            mostrar_mensaje_subrayado("¡Producto actualizado exitosamente!")  # Confirmación de éxito
        else:
            mostrar_mensaje_subrayado("Error al actualizar el producto.", Fore.RED)  # Mensaje de error
    else:
        mostrar_mensaje_subrayado("No existe un producto con el ID ingresado.", Fore.RED)  # Si no se encuentra el producto

# Función para eliminar un producto
def opcion_eliminar_producto():
    """
    Permite al usuario eliminar un producto tras confirmar la acción.
    """
    id = leerInt("Ingrese el id del producto a eliminar: ")
    fue_eliminado = eliminar_producto(id)  # Intenta obtener y eliminar el producto

    if fue_eliminado:
        mostrar_mensaje_subrayado("Producto eliminado con éxito.")  # Confirmación de éxito
    else:
        mostrar_mensaje_subrayado("No se pudo eliminar el producto con el id ingresado.", Fore.RED)  # Producto no encontrado

# Función para buscar un producto por ID
def opcion_buscar_producto():
    """
    Solicita el ID de un producto y muestra la información si existe.
    """
    id = leerInt("Ingrese el ID del producto que desea buscar: ")
    producto = obtener_productos_por_id(id)
    
    if producto:
        mostrar_mensaje_subrayado("------ Lista de Productos ------")
        imprimir_producto(producto)  # Muestra la información del producto
    else:
        mostrar_mensaje_subrayado("Producto no encontrado en el inventario.", Fore.RED)  # Producto no encontrado

# Función para generar reporte de productos con bajo stock
def opcion_reporte_bajo_stock():
    """
    Genera un reporte de productos cuya cantidad en stock es inferior a un mínimo especificado.
    """
    minimo_stock = leerInt("Ingrese el mínimo de stock para el reporte: ")
    inventario = reporte_bajo_stock(minimo_stock)  # Obtiene productos con bajo stock
    productos_bajo_stock = [p for p in inventario if p['cantidad'] < minimo_stock]  # Filtra productos con bajo stock

    if productos_bajo_stock:
        mostrar_mensaje_subrayado("Reporte de Productos con Bajo Stock")
        for producto in productos_bajo_stock:  # Muestra cada producto con bajo stock
            imprimir_producto(producto)
    else:
        print("No hay productos con bajo stock.")  # Mensaje si no hay productos con bajo stock

# ******************************************************************
# INVOCAMOS A LA FUNCIÓN PRINCIPAL
# ******************************************************************

# Iniciar el programa
iniciar_programa()