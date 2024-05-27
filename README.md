# App-Movil-Filtros
Proyecto Cómputo Paralelo

Este proyecto desarrolla una aplicación móvil similar a Instagram que permite a los usuarios aplicar tres filtros personalizados a sus imágenes utilizando algoritmos de convolución y PyCUDA para aprovechar la potencia de procesamiento de la GPU. La aplicación incluye una API para el procesamiento de imágenes y se dockeriza junto con una base de datos.

## Descripción del Proyecto

### Funcionalidades

Filtros Personalizados:


Realce de Colores


### API en Flask:

Recibe imágenes y aplica los filtros utilizando PyCUDA. 

Devuelve la imagen filtrada al cliente.


### Base de Datos PostgreSQL:

Almacena información de los usuarios y las imágenes.


### Dockerización:

La API y la base de datos están dockerizadas para facilitar su despliegue.

### Aplicación Móvil en Flutter:

Permite a los usuarios seleccionar imágenes, aplicar filtros y ver el resultado.


### Requisitos

- Tecnologías Utilizadas

- Frontend móvil: Flutter

- Backend: Python (Flask)

- Procesamiento de Imágenes: PyCUDA

- Base de Datos: PostgreSQL

- Contenedorización: Docker
