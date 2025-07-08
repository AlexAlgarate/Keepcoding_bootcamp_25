import pytest

import main as main


def test_descomponer_numeros():
    assert main.split_number(1976) == [1000, 900, 70, 6]
    assert main.split_number(2984) == [2000, 900, 80, 4]


@pytest.mark.parametrize(
    "input_values, expected_values",
    [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (2564, "MMDLXIV"),
        (3999, "MMMCMXCIX"),
        (150, "CL"),
    ],
)
def test_int_to_roman(input_values, expected_values):
    assert main.int_to_roman(input_values, main.roman_numeral_dict) == expected_values


def test_int_to_roman_raises_exception_number_zero():
    with pytest.raises(
        ValueError, match="No existen números romanos para valores ≤ 0."
    ):
        main.int_to_roman(0, main.roman_numeral_dict)


def test_int_to_roman_raises_exception_number_grater_than_4000():
    with pytest.raises(
        ValueError, match="Los números romanos tradicionales llegan hasta 3999."
    ):
        main.int_to_roman(4000, main.roman_numeral_dict)
