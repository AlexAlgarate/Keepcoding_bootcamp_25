def make_reciprocate(numbers: list) -> list[float | None]:
    converted: list = []
    for number in numbers:
        if number == 0:
            converted.append(None)
        else:
            converted.append(1 / number)
    return converted


def make_reciprocate_list(numbers: list) -> list[int | None]:
    return [None if number == 0 else 1 / number for number in numbers]


def elevate(numbers: list, exponent: int) -> list[int]:
    return [number**exponent for number in numbers]


# print(elevate([1, 2, 3, 4, 5, 0], 4))


"""

Escribe una función smart_rle_compress que tome una cadena de texto y devuelva otra donde 
las repeticiones consecutivas se comprimen solo si la versión comprimida es más corta.

Reglas:
Si una letra aparece más de 2 veces seguidas, reemplázala por <letra><número>
Si aparece 1 o 2 veces, se deja tal cual
Conserva el orden del texto original
Ejemplos:
"hhhoollllla" → "h3ool5a"
"hellooo" → "hello3"
"aabbcc" → "aabbcc"
"baaaad" → "ba4d"

"""
word = "hhhooolaaa"


def smart_rle_compress(cadena):
    def procesa_cambio(contador, recuerdo):
        if contador <= 2:
            result = recuerdo * contador
        else:
            result = recuerdo + str(contador)
        return result

    recuerdo = ""
    contador = 1
    resultado = ""

    for car in cadena:
        if car == recuerdo:
            contador += 1
        else:
            resultado += procesa_cambio(contador, recuerdo)

            recuerdo = car
            contador = 1

    resultado += procesa_cambio(contador, recuerdo)

    return resultado


print(smart_rle_compress(word))
list_of_numbers = [72, 72, 75, 75, 70, 74, 74, 76]


def detectar_indices(lista_numeros: list[int]):
    result = []

    for number in range(len(lista_numeros) - 1):
        if lista_numeros[number] != lista_numeros[number + 1]:
            result.append((number, number + 1))

    return result


print(detectar_indices(list_of_numbers))


def detectar_cambios(lista):
    cambios = []
    for i in range(len(lista) - 1):
        if lista[i] != lista[i + 1]:
            cambios.append((i, i + 1))
    return cambios
