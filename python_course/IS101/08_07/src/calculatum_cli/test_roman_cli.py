import pytest
from pytest import MonkeyPatch

from src.roman_number import RomanNumber as RN

from .application import calculate_operation
from .domain import Operation
from .infrastructure import (
    continue_or_exit,
    input_number,
    input_operation,
)


@pytest.mark.parametrize(
    "user_input, expected_roman_number",
    [
        (["I"], RN(1)),
        (["doce", "-1", "XII"], RN(12)),
        (["12"], RN(12)),
    ],
)
def test_roman_inputs(
    monkeypatch, user_input: list[str], expected_roman_number: RN
) -> None:
    inputs = iter(user_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert input_number("") == expected_roman_number


@pytest.mark.parametrize(
    "user_input, expected_operation",
    [
        (["+"], Operation.ADD),
        (["-"], Operation.SUB),
        (["x"], Operation.MUL),
        (["/"], Operation.DIV),
        (["*", "x"], Operation.MUL),
    ],
)
def test_input_operations(
    monkeypatch: MonkeyPatch, user_input: list[str], expected_operation: Operation
) -> None:
    inputs = iter(user_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert input_operation("") == expected_operation


@pytest.mark.parametrize(
    "roman_num1, roman_num2, expected_result, operation",
    [
        (RN(1), RN(32), RN(33), Operation.ADD),
        (RN(41), RN(32), RN(9), Operation.SUB),
        (RN(1), RN(32), RN(32), Operation.MUL),
        (RN(32), RN(32), RN(1), Operation.DIV),
    ],
)
def test_calculate_operation(
    roman_num1: RN, roman_num2: RN, expected_result: RN, operation: Operation
) -> None:
    assert calculate_operation(roman_num1, roman_num2, operation) == expected_result


@pytest.mark.parametrize(
    "user_response, expected_continue",
    [
        ("S", True),
        ("s", True),
        ("N", False),
        ("n", False),
        ("12", False),
    ],
)
def test_continue_or_exit(
    monkeypatch: MonkeyPatch, user_response: str, expected_continue: bool
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: user_response)
    assert continue_or_exit("") == expected_continue
