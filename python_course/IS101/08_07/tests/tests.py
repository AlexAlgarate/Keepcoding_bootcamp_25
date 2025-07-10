import pytest

from main import from_arabic_to_roman, from_roman_to_arabic


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
def test_int_to_roman(input_values: int, expected_values: str) -> None:
    assert from_arabic_to_roman(input_values) == expected_values


@pytest.mark.parametrize(
    "not_valid_number",
    [0, 4000],
)
def test_int_to_roman_raises_exception_not_valid_number(not_valid_number: int) -> None:
    with pytest.raises(ValueError, match="El número tiene que estar entre 0 y 3999."):
        from_arabic_to_roman(not_valid_number)


def test_int_to_roman_raises_exception_number_grater_than_4000() -> None:
    with pytest.raises(ValueError, match="El número tiene que estar entre 0 y 3999."):
        from_arabic_to_roman(4000)


@pytest.mark.parametrize(
    "input_values, expected_values",
    [
        ("I", 1),
        ("X", 10),
        ("M", 1000),
        ("MDLV", 1555),
        ("DCLXVI", 666),
        ("dclxvi", 666),
    ],
)
def test_roman_to_int(input_values: str, expected_values: int) -> None:
    assert from_roman_to_arabic(input_values) == expected_values


@pytest.mark.parametrize(
    "roman",
    [
        "A",
        "BXI",
        "123",
        "!",
        "MMMMM",
        " ",
        "IL",
        "xm",
        "VX",
    ],
)
def test_invalid_roman_value_raises_error(roman: str) -> None:
    with pytest.raises(ValueError, match="romano no válido"):
        from_roman_to_arabic(roman)
