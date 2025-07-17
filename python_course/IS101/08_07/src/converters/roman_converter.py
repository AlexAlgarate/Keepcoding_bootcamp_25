from src.constants.constants import ARABIC_TO_ROMAN_MAP
from src.converters.converter_interface import IRomanCalculator
from src.converters.extended_converter import ExtendedRomanConverter
from src.converters.standard_converter import StandardRomanConverter
from src.converters.utils.roman_validator import RomanNumeralValidator


class RomanConverter(IRomanCalculator):
    def __init__(self) -> None:
        self._standard_converter = StandardRomanConverter(ARABIC_TO_ROMAN_MAP)
        self._extended_converter = ExtendedRomanConverter(self._standard_converter)

    def to_roman(self, number: int) -> str:
        validate_number = RomanNumeralValidator.validate_arabic_input(number)
        return self._extended_converter.to_roman(validate_number)

    def to_arabic(self, roman: str) -> int:
        validate_roman = RomanNumeralValidator.validate_roman_input(roman)
        return self._extended_converter.to_arabic(validate_roman)


def create_roman_calculator() -> RomanConverter:
    return RomanConverter()
