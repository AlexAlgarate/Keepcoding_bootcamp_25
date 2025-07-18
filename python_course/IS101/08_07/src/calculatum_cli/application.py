from src.roman_number import RomanNumber as RN

from .domain import Operation


def calculate_operation(number_1: RN, number_2: RN, operation: Operation) -> RN:
    return operation.calculate_operation(number_1, number_2)
