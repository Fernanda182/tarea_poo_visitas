# Sistema de Registro de Visitantes

## Autor:
Fernanda Vaca

## Objetivo

Desarrollar una aplicación con interfaz gráfica que permita registrar y gestionar visitantes, separando correctamente la lógica de negocio, la interfaz y los modelos de datos mediante Programación Orientada a Objetos (POO).

## Funcionalidades

✔ Registrar nuevos visitantes

✔ Visualizar visitantes en una tabla dinámica

✔ Eliminar visitantes seleccionados

✔ Limpiar campos del formulario

✔ Validar campos vacíos

✔ Evitar registro de cédulas duplicadas

## Arquitectura del Proyecto

El sistema está organizado en capas para mantener una estructura clara y escalable:

VISITAS_APP/
│
├── main.py
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
    └── app_tkinter.py
    
## Tecnologías Utilizadas

Python 

Tkinter 

## Conceptos Aplicados

Programación Orientada a Objetos 

- Encapsulamiento
- Inyección de dependencias
- Arquitectura modular por capas

## Cómo ejecutar el programa

- Descargar o clonar el repositorio
- Abrir la carpeta en Visual Studio Code
- Ejecutar el archivo principal:
- python main.py

## Notas

- La información se almacena en memoria
- La aplicación valida errores comunes como campos vacíos o cédulas duplicadas
