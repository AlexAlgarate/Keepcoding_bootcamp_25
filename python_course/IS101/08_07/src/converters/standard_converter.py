from types import MappingProxyType

from src.constants.constants import ROMAN_TO_ARABIC_MAP
from src.constants.constants import MinMaxValues as values
from src.converters.utils.roman_validator import RomanNumeralValidator


class StandardRomanConverter:
    def __init__(self, mapping: dict):
        self._arabic_to_roman = MappingProxyType(mapping)
        self._roman_to_arabic = MappingProxyType(ROMAN_TO_ARABIC_MAP)

    def to_roman(self, number: int) -> str:
        if (
            not values.MIN_ROMAN_VALUE.value
            <= number
            <= values.MAX_STANDARD_ROMAN.value
        ):
            raise ValueError(
                f"Número fuera del rango ({values.MIN_ROMAN_VALUE.value}-{values.MAX_STANDARD_ROMAN.value}): {number}"
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
            raise ValueError(f"Número romano inválido: '{roman}'")

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
