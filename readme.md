### main
Contiene la lógica a llevar entre la vista y el modulo de base de datos

### Base de datos:
contiene el array o la conex a sqlite

## vista:
solo muestra o pide datos

## Proyecto de Gestión de Inventario:
Este proyecto permite gestionar un inventario de productos utilizando una base de datos SQLite. A través de una interfaz de consola, el usuario puede agregar, mostrar, actualizar, eliminar productos, realizar búsquedas y generar reportes de productos con bajo stock.

## Requisitos
Python 3.x
SQLite (ya integrado en Python)

## Instalación
Clona o descarga este repositorio.

Asegúrate de tener Python 3.x instalado en tu máquina.

Instala las dependencias necesarias con el siguiente comando:

Copiar código
pip install colorama

El archivo de la base de datos se llamará inventario.db y se creará automáticamente cuando se ejecute el programa.

## Estructura del Proyecto
El proyecto está compuesto por los siguientes módulos:

Funciones_vista.py: Contiene las funciones relacionadas con la interfaz de usuario (mostrar menús, leer entradas, mostrar productos).

Funciones_database.py: Contiene las funciones para interactuar con la base de datos (crear tablas, insertar, actualizar, eliminar productos).

## Funciones Principales

## Menú Principal
El programa ofrece un menú interactivo con las siguientes opciones:

Agregar producto
Mostrar productos
Actualizar cantidad de producto
Eliminar producto
Buscar producto
Reporte de productos con bajo stock
Salir

## Base de Datos
El programa interactúa con una base de datos SQLite (inventario.db), donde se almacenan los productos. Las siguientes acciones pueden realizarse:

Crear tabla de productos: Si no existe, se crea la tabla productos con los campos id, nombre, descripcion, categoria, cantidad y precio.

Registrar producto: Permite agregar un producto nuevo a la base de datos.

Obtener todos los productos: Muestra todos los productos registrados.

Obtener producto por ID: Permite obtener un producto específico por su id.

Actualizar producto: Actualiza la cantidad y el precio de un producto.

Eliminar producto: Elimina un producto de la base de datos por su id.

Generar reporte de bajo stock: Muestra los productos que tienen una cantidad menor al stock mínimo especificado.

## Uso
Ejecuta el archivo principal del proyecto.

Se mostrará el menú con las opciones disponibles.

Ingresa la opción que deseas ejecutar y sigue las instrucciones que se muestren en pantalla.
