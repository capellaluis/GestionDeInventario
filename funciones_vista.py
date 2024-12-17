from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Función que muestra el menú principal del programa con color azul
def mostrar_menu():
    """
    Muestra el menú principal de opciones para la gestión de productos.
    Incluye opciones para agregar, mostrar, actualizar, eliminar productos,
    buscar productos, generar reporte de bajo stock y salir.
    """
    # Toda la sección del menú será azul
    print(f"{Fore.BLUE}\n--- Menú de Gestión de Productos ---")
    print(f"{Fore.BLUE}1. Agregar producto")
    print(f"{Fore.BLUE}2. Mostrar productos")
    print(f"{Fore.BLUE}3. Actualizar cantidad de producto")
    print(f"{Fore.BLUE}4. Eliminar producto")
    print(f"{Fore.BLUE}5. Buscar producto")
    print(f"{Fore.BLUE}6. Reporte de productos con bajo stock")
    print(f"{Fore.BLUE}7. Salir\n")

# Función para leer una cadena de texto (str) con validación de entrada
def leerString(mensaje):
    """
    Lee una cadena de texto del usuario.
    Parámetro:
        - mensaje (str): Mensaje que se muestra al usuario para pedir la entrada.
    Retorna:
        - La cadena de texto ingresada por el usuario.
    """
    return input(mensaje)

# Función para leer un número entero (int) con validación
def leerInt(mensaje):
    """
    Lee un número entero del usuario, asegurándose de que la entrada sea válida.
    Si el usuario ingresa algo que no es un número entero, muestra un mensaje de error y vuelve a solicitar la entrada.
    Parámetro:
        - mensaje (str): Mensaje que se muestra al usuario para pedir la entrada.
    Retorna:
        - Un número entero ingresado por el usuario.
    """
    while True:
        try:
            return int(input(mensaje))  # Intenta convertir la entrada a un número entero
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")  # Si ocurre un error, muestra un mensaje y repite el ciclo

# Función para leer un número decimal (float) con validación
def leerFloat(mensaje):
    """
    Lee un número decimal (float) del usuario, asegurándose de que la entrada sea válida.
    Si el usuario ingresa algo que no es un número decimal, muestra un mensaje de error y vuelve a solicitar la entrada.
    Parámetro:
        - mensaje (str): Mensaje que se muestra al usuario para pedir la entrada.
    Retorna:
        - Un número decimal ingresado por el usuario.
    """
    while True:
        try:
            return float(input(mensaje))  # Intenta convertir la entrada a un número decimal
        except ValueError:
            print("Error: Por favor, ingresa un número decimal válido.")  # Si ocurre un error, muestra un mensaje y repite el ciclo

# Función para mostrar mensajes con un estilo subrayado (en verde)
def mostrar_mensaje_subrayado(mensaje, color = Fore.GREEN ):
    """
    Muestra un mensaje con un estilo de subrayado, usando asteriscos.
    Parámetro:
        - mensaje (str): El mensaje que se va a mostrar.
    """
    print(f"{color}{'*' * 50}")  # Imprime una línea de 50 asteriscos antes del mensaje
    print(f"{color}{mensaje}")  # Muestra el mensaje proporcionado
    print(f"{color}{'*' * 50}")  # Imprime una línea de 50 asteriscos después del mensaje


# Función para imprimir un producto detallado (en verde)
def imprimir_producto(producto):
    """
    Imprime los detalles completos de un producto, incluyendo su ID, nombre, descripción, cantidad,
    precio y categoría.
    Parámetro:
        - producto (dict): Un diccionario que contiene los detalles del producto (id, nombre, descripción, cantidad, precio, categoría).
    """
    print(f"{Fore.GREEN}{producto['id']}. {producto['nombre']} - {producto['descripcion']} - "
          f"Cantidad: {producto['cantidad']} - Precio: ${producto['precio']:.2f} - "
          f"Categoría: {producto['categoria']}")
