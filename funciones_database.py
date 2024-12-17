import sqlite3

# DECLARACION DE CONSTANTES
ruta_db = "inventario.db"

# Función para crear la tabla 'productos' si no existe
def db_crear_tabla_productos():
    """
    Crea la tabla 'productos' en la base de datos si no existe.
    La tabla contiene los campos: id, nombre, descripcion, categoria, cantidad y precio.
    """
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()  
    cursor.execute(
    """ 
        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        categoria TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
        )
    """
    )
    conexion.commit()

# Función para registrar un producto en la base de datos
def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    """
    Inserta un nuevo producto en la tabla 'productos'.
    Parámetros:
        - nombre (str): Nombre del producto.
        - descripcion (str): Descripción del producto.
        - cantidad (int): Cantidad disponible.
        - precio (float): Precio del producto.
        - categoria (str): Categoría a la que pertenece el producto.
    Retorna:
        - True si la operación es exitosa, False si ocurre un error.
    """
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        query = "INSERT INTO productos VALUES (NULL, ?, ?, ?, ?, ?)"
        parametros = (nombre, descripcion, categoria, cantidad, precio)
        cursor.execute(query, parametros)
        conexion.commit()
        return True
    except Exception:
        return False
    finally:
        conexion.close()

# Función para obtener todos los productos de la tabla
def todos_productos():
    """
    Recupera todos los productos almacenados en la tabla 'productos'.
    Retorna:
        - Una lista de diccionarios, donde cada diccionario representa un producto.
        - Retorna una lista vacía si ocurre un error.
    """
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        query = "SELECT * FROM productos"
        cursor.execute(query)
        columnas = [col[0] for col in cursor.description]  # Nombres de columnas
        lista_productos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
        return lista_productos
    except Exception:
        return []
    finally:
        conexion.close()

# Función para obtener un producto específico por su ID
def obtener_productos_por_id(id):
    """
    Recupera un producto específico usando su ID.
    Parámetros:
        - id (int): ID del producto a buscar.
    Retorna:
        - Un diccionario con los datos del producto si se encuentra.
        - None si no se encuentra el producto o ocurre un error.
    """
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()  
        query = "SELECT * FROM productos where id = ?"
        cursor.execute(query, (id,))
        columnas = [col[0] for col in cursor.description]  # Obtener los nombres de las columnas
        fila_producto = cursor.fetchone()  # Obtener la fila del producto        
        if fila_producto:
            producto = dict(zip(columnas, fila_producto))  # Convertir la fila en un diccionario
            return producto
        return None
    except Exception:
        return None
    finally:
        conexion.close()

# Función para actualizar la cantidad y el precio de un producto
def actualizar_producto(id, nueva_cantidad, nuevo_precio):
    """
    Actualiza la cantidad y el precio de un producto identificado por su ID.
    Parámetros:
        - id (int): ID del producto a actualizar.
        - nueva_cantidad (int): Nueva cantidad del producto.
        - nuevo_precio (float): Nuevo precio del producto.
    Retorna:
        - True si la operación es exitosa, False si ocurre un error.
    """
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        query = "UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?"
        parametros = (nueva_cantidad, nuevo_precio, id)
        cursor.execute(query, parametros)
        conexion.commit()
        return True
    except sqlite3.Error:
        return False
    finally:
        conexion.close()

# Función para eliminar un producto de la base de datos por su ID
def eliminar_producto(id):
    """
    Elimina un producto de la tabla 'productos' utilizando su ID.
    Parámetros:
        - id (int): ID del producto a eliminar.
    """
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = ?"
        parametros = (id,)
        cursor.execute(query, parametros)
        conexion.commit()
        return cursor.rowcount != 0 # True si borró el registro, False en caso contrario
    except Exception as error:
        return False
    finally:
        conexion.close()

# Función para generar un reporte de productos con bajo stock
def reporte_bajo_stock(minimo_stock):
    """
    Genera un reporte de productos con cantidad menor al mínimo especificado.
    Parámetros:
        - minimo_stock (int): Límite de stock mínimo.
    Retorna:
        - Una lista de diccionarios con los productos que cumplen la condición.
    """
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        query = "SELECT * FROM productos WHERE cantidad < ?"
        cursor.execute(query, (minimo_stock,))
        columnas = [col[0] for col in cursor.description]  # Nombres de columnas
        lista_productos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
        return lista_productos
    except Exception:
        return []
    finally:
        conexion.close()

