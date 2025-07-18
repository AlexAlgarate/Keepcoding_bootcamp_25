from enum import Enum

from src.roman_number import RomanNumber as RN


class Operation(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"

    def calculate_operation(self, num1: RN, num2: RN) -> RN:
        if self == Operation.ADD:
            resultado = num1 + num2
        elif self == Operation.SUB:
            resultado = num1 - num2
        elif self == Operation.MUL:
            resultado = num1 * num2
        elif self == Operation.DIV:
            resultado = num1 / num2
        return resultado
