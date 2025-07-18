from src.roman_number import RomanNumber as RN


def input_number(message: str) -> RN:
    while True:
        cadena = input(message).upper()
        try:
            if cadena.isdigit():
                cadena = int(cadena)
            numero = RN(cadena)
            break
        except ValueError:
            print("Numero Romano/Entero no valido")

    return numero


def input_operation(message: str):
    pass


def continue_or_exit(message: str) -> bool:
    return input(message).lower() == "s"
