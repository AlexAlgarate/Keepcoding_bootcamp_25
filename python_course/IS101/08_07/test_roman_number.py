from typing import Any

import pytest

from src.roman_number import RomanNumber as rn


@pytest.mark.parametrize(
    "arabic_number, roman_repr", [(10, "X"), ("XII", "XII"), (12 + 23, "XXXV")]
)
def test_print_numeros_romanos(arabic_number: int, roman_repr: str) -> None:
    assert str(rn(arabic_number)) == roman_repr


@pytest.mark.parametrize(
    "op1, op2, operation, result",
    [
        (rn(1), rn(3), lambda a, b: a + b, rn(4)),
        (rn(3), rn(1), lambda a, b: a - b, rn(2)),
        (rn(1), rn(3), lambda a, b: a * b, rn(3)),
        (rn(5), rn(3), lambda a, b: a / b, rn(1)),
        (rn(5), rn(3), lambda a, b: a % b, rn(2)),
        (rn(3), rn(4), lambda a, b: a**b, rn(81)),
        (rn(1), 3, lambda x, y: x + y, rn(4)),
        (rn(3), 1, lambda x, y: x - y, rn(2)),
        (rn(1), 3, lambda x, y: x * y, rn(3)),
        (rn(5), 3, lambda x, y: x / y, rn(1)),
        (rn(5), 3, lambda x, y: x % y, rn(2)),
        (rn(3), 4, lambda x, y: x**y, rn(81)),
        (1, rn(3), lambda x, y: x + y, rn(4)),
        (3, rn(1), lambda x, y: x - y, rn(2)),
        (1, rn(3), lambda x, y: x * y, rn(3)),
        (5, rn(3), lambda x, y: x / y, rn(1)),
        (5, rn(3), lambda x, y: x % y, rn(2)),
        (3, rn(4), lambda x, y: x**y, rn(81)),
    ],
)
def test_operacion(op1: rn | int, op2: rn | int, operation: Any, result: Any) -> None:
    assert operation(op1, op2) == result
