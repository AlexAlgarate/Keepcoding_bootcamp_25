import pytest

from main import (
    ARABIC_TO_ROMAN_MAP,
    ROMAN_TO_ARABIC_MAP,
    RomanCalculator,
    create_roman_calculator,
    from_arabic_to_roman,
    from_roman_to_arabic,
)


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


class TestRomanCalculator:
    @pytest.fixture
    def calculator(self) -> RomanCalculator:
        return create_roman_calculator(ARABIC_TO_ROMAN_MAP, ROMAN_TO_ARABIC_MAP)

    @pytest.fixture
    def conversion_cases(self) -> list[tuple[int, str]]:
        return [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (27, "XXVII"),
            (48, "XLVIII"),
            (59, "LIX"),
            (93, "XCIII"),
            (141, "CXLI"),
            (163, "CLXIII"),
            (402, "CDII"),
            (575, "DLXXV"),
            (911, "CMXI"),
            (1024, "MXXIV"),
            (1234, "MCCXXXIV"),
            (1549, "MDXLIX"),
            (3000, "MMM"),
            (3999, "MMMCMXCIX"),
        ]

    def test_valid_conversions_arabic_to_roman(
        self, calculator, conversion_cases: list[tuple[int, str]]
    ) -> None:
        for number, expected_roman in conversion_cases:
            assert calculator.from_arabic_to_roman(number) == expected_roman

    def test_valid_conversions_roman_to_arabic(
        self, calculator, conversion_cases: list[tuple[int, str]]
    ) -> None:
        for expected_number, roman in conversion_cases:
            assert calculator.from_roman_to_arabic(roman) == expected_number
