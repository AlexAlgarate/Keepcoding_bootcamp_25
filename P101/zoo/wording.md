# Ejercicio Zoo: Cálculo del Precio de Entrada para un Grupo en el Zoológico

## Objetivo

Desarrollar un programa que calcule el precio total de entrada para un grupo de visitantes a un zoológico basado en sus edades. El programa debe también proporcionar un desglose detallado de los precios por edad.

## Reglas de Precios

- Niños de 2 años o menos: Entrada gratuita.
- Niños de 3 a 12 años: 14 euros.
- A partir de 13 años (adultos): 23 euros.
- Jubilados (65 años o más): 18 euros.

## Instrucciones

1. Entrada de Datos:

    - El programa debe solicitar las edades de los miembros del grupo uno por uno.
    - La entrada de datos debe terminar cuando se introduzca una cadena vacía.

2. Validación:

    - Asegúrate de que las edades ingresadas sean números enteros y positivos.

3. Cálculo del Precio:

    - Calcula el precio total del grupo basado en las reglas de precios.
    - Proporciona un desglose detallado del costo por cada rango de edad.

4. Salida de Datos:

    - Al finalizar la entrada de datos, muestra el precio total del grupo.
    - Muestra el desglose detallado de los precios por edad.

## Ayuda para la Implementación

Puedes utilizar estructuras de datos como listas o tuplas para almacenar las edades y los precios mientras se ingresan.

Ejemplo de Ejecución:

    1. Introduce la edad del visitante (deja vacío para terminar): 5
    2. Introduce la edad del visitante (deja vacío para terminar): 30
    3. Introduce la edad del visitante (deja vacío para terminar): 70
    4. Introduce la edad del visitante (deja vacío para terminar):
    5. Precio total del grupo: 55 euros
    6. Detalle por edades:
    7. Niños (3-12 años): 1 x 14 euros = 14 euros
    8. Adultos (13-64 años): 1 x 23 euros = 23 euros
    9. Jubilados (65+ años): 1 x 18 euros = 18 euros
    

## Consideraciones Finales

- Asegúrate de que el programa maneje correctamente entradas no válidas y que solicite la edad nuevamente si se introduce un valor incorrecto.
- El programa debe ser fácil de usar y proporcionar resultados claros y precisos.
