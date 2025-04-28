# Proyecto Backend CRUD de UrbanaIconic 
 
Este proyecto es un backend que implementa las operaciones CRUD (Create, Read, Update, Delete) para gestionar productos. Utiliza Flask como framework web para Python. 
 
## Requisitos 
 
- Python 3.x 
- Flask 
- Flask-CORS 


## Instalación 
 
1. Clona este repositorio. 
2. Se recomienda usar un entorno virtual (virtualenv o venv).
3. Instala las dependencias con  pip install -r requirements.txt . 


## Configuración del Entorno

- Crear un archivo .env en la raíz del proyecto y configurar las variables de entorno necesarias.


## Ejecución 
 
1. Ejecuta el archivo  run.py  para iniciar el servidor. 
2. El servidor estará disponible en  http://127.0.0.1:5000/ . 
 

## Endpoints 
 
-  GET /api/products/ : Obtiene todos los productos. 
-  POST /api/products/ : Crea un nuevo producto. 
-  GET /api/products/<product_id> : Obtiene un producto específico. 
-  PUT /api/products/<product_id> : Actualiza un producto existente. 
-  DELETE /api/products/<product_id> : Elimina un producto.

## Estado del proyecto

En desarrollo.
Pensado como base para un sistema de gestión de productos con API RESTful.
