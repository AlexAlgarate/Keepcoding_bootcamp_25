from types import MappingProxyType

from . import roman_exceptions as exc
from .validators.roman_validator import RomanNumeralValidator

ARABIC_TO_ROMAN_MAP: dict[int, str] = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

ROMAN_TO_ARABIC_MAP: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class StandardRomanConverter:
    MIN_ROMAN_VALUE = 1
    MAX_STANDARD_ROMAN = 3999

    def __init__(self, mapping: dict):
        self._arabic_to_roman = MappingProxyType(mapping)
        self._roman_to_arabic = MappingProxyType(ROMAN_TO_ARABIC_MAP)

    def to_roman(self, number: int) -> str:
        if not self.MIN_ROMAN_VALUE <= number <= self.MAX_STANDARD_ROMAN:
            raise exc.NumberOutOfRangeError(
                f"Número fuera del rango ({self.MIN_ROMAN_VALUE}-{self.MAX_STANDARD_ROMAN}): {number}"
            )
        result = []
        for value, numeral in self._arabic_to_roman.items():
            count, number = divmod(number, value)
            if count:
                result.append(numeral * count)
        return "".join(result)

    def to_arabic(self, roman: str) -> int:
        roman = RomanNumeralValidator.validate_roman_input(roman)
        if not RomanNumeralValidator.is_valid_roman(roman):
            raise exc.InvalidRomanNumeralError(f"Número romano inválido: '{roman}'")
        result = 0
        previous = 0
        for char in reversed(roman):
            value = self._roman_to_arabic[char]
            if value < previous:
                result -= value
            else:
                result += value
                previous = value
        return result
