"""
1. Elevar al cuadrado
Transforma una lista de números en una lista de sus cuadrados.
2. Longitudes de palabras
Dada una lista de palabras, devuelve una lista con sus longitudes.
3. Capitalizar nombres
Convierte una lista de nombres en minúsculas a nombres con la primera
letra en mayúscula.
4. Euros a dólares
Convierte una lista de precios en euros a dólares (usa un tipo fijo, p. ej.
1€ = 1.1$).
5. Invertir booleanos
Dada una lista de valores True y False , devuelve la lista con los
valores invertidos.
"""

from functools import reduce

list_numbers = [-5, -4, -3, -3, -2, -1, 0, 1, 2, 3, 4, 5]
list_words = ["hello", "world", "keepcoding", "alex", "elefante"]
list_prices = [1, 10, 100]
list_booleans = [True, False, False, True, True]
list_booleans_with_None = [None, True, False, 1, "HELLO", True, None]

print("\nMAP\n")
print("1. Elevar al cuadrado -->", list(map(lambda x: x**2, list_numbers)))
print("2. Longitudes de palabras -->", list(map(lambda x: len(x), list_words)))
print("3. Capitalizar nombres -->", list(map(lambda x: x.capitalize(), list_words)))
print(
    "4. Euros a dólares -->", list(map(lambda x: f"{round(x * 1.1, 2)}$", list_prices))
)
print("5. Invertir booleanos -->", list(map(lambda x: not x, list_booleans)))

"""

filter – Seleccionar elementos
1. Filtrar pares
Dada una lista de enteros, devuelve sólo los números pares.
2. Palabras largas
Dada una lista de palabras, filtra aquellas que tengan más de 5 letras.
3. Eliminar valores nulos
Filtra de una lista los elementos que sean None .
4. Solo booleanos verdaderos
De una lista de expresiones booleanas, filtra los True .
5. Números positivos
De una lista de enteros, conserva solo los mayores que cero
"""
print("\nFILTER\n")
print("1. Filtrar pares -->", list(filter(lambda x: x % 2 == 0, list_numbers)))
print("2. Palabras largas -->", list(filter(lambda x: len(x) > 5, list_words)))
print(
    "3. Eliminar valores nulos -->",
    list(filter(lambda x: x is not None, list_booleans_with_None)),
)
print("4. Solo booleanos verdaderos -->", list(filter(lambda x: x, list_booleans)))
print("5. Números positivos -->", list(filter(lambda x: x > 0, list_numbers)))

"""
reduce – Acumular valores
Nota: requiere importar reduce de functools .
1. Suma total
Suma todos los elementos de una lista de números.
2. Producto total
Calcula el producto de todos los elementos.
3. Concatenar strings
Concatena una lista de palabras en una sola cadena.
4. Encontrar el máximo
Devuelve el valor máximo de una lista sin usar max .
5. Contar ocurrencias
Dada una lista de valores booleanos, cuenta cuántos son True .
"""
list_numbers = [1, 2, 3, 4, 5]
list_words = ["hello", "world", "keepcoding", "alex", "elefante"]
list_booleans = [True, False, False, True, True]

print("\nREDUCE\n")
print("1. Suma total -->", reduce(lambda x, y: x + y, list_numbers))
print("2. Producto total -->", reduce(lambda x, y: x * y, list_numbers))
print("3. Concatenar strings -->", reduce(lambda x, y: x + y, list_words))
print(
    "4. Encontrar el máximo -->", reduce(lambda x, y: x if x > y else y, list_numbers)
)
print(
    "5. Contar ocurrencias -->",
    reduce(lambda acc, x: acc + (1 if x is True else 0), list_booleans, 0),
)
"""
Combinaciones de map , filter y reduce –
5 ejercicios
1. Doblar los pares y sumarlos
Dada una lista de enteros, filtra los pares, duplícalos y suma el resultado
total.
2. Contar palabras largas
Dada una lista de palabras, filtra las que tienen más de 4 letras y cuenta
cuántas son.
3. Suma de cuadrados de impares
Filtra los impares de una lista de números, elévalos al cuadrado y
devuelve la suma total.
4. Promedio de edades válidas
Dada una lista de edades (puede incluir None o valores negativos), filtra
las válidas (enteros ≥ 0), y calcula el promedio (suma con reduce ,
dividido por cantidad).
5. Concatenar nombres cortos en mayúsculas
Dada una lista de nombres, filtra los que tienen 4 letras o menos,
conviértelos a mayúsculas y concaténalos en una sola cadena separada
por comas.
"""
list_numbers = [1, 2, 3, 4, 5]
list_ages = [-10, None, 10, 20]
list_words = ["hello", "world", "keepcoding", "pau", "Lara"]
list_booleans = [True, False, False, True, True]

print("\nCOMBINACION\n")
print(
    "1. Doblar los pares y sumarlos -->",
    reduce(
        lambda x, y: x + y,
        map(lambda x: x * 2, filter(lambda x: x % 2 == 0, list_numbers)),
    ),
)
print(
    "2. Contar palabras largas -->",
    list(map(lambda x: len(x), filter(lambda x: len(x) > 4, list_words))),
)

print(
    "3. Suma de cuadrados de impares --> ",
    reduce(
        lambda x, y: x + y,
        map(lambda x: x**2, filter(lambda x: x % 2 == 1, list_numbers)),
    ),
)

print(
    "4. Promedio de edades válidas --> ",
    (
        lambda edades: reduce(lambda x, y: x + y, edades) / len(edades)
        if edades
        else None
    )(list(filter(lambda x: x is not None and x >= 0, list_ages))),
)

print(
    "5. Concatenar nombres cortos en mayúsculas --> ",
    ",".join(
        map(lambda x: x.upper(), filter(lambda x: len(x) <= 4, list_words)),
    ),
)
