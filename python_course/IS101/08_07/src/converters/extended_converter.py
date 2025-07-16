from src.constants.constants import ARABIC_TO_ROMAN_MAP, ROMAN_TO_ARABIC_MAP
from src.constants.constants import MinMaxValues as values
from src.utils import roman_exceptions as exc
from src.utils.roman_validator import RomanNumeralValidator

from .converter_interface import IRomanCalculator
from .standard_converter import StandardRomanConverter


class ExtendedRomanProcessor(IRomanCalculator):
    THOUSAND_INDICATOR = "•"

    def __init__(self, standard_converter: StandardRomanConverter):
        self._standard_converter = standard_converter

    def split_into_thousands(self, number: int) -> list[int]:
        if number == 0:
            return [0]

        result = []
        while number > 0:
            resto = number % 1000
            result.append(resto)
            number //= 1000

        if result[-1] < 4 and len(result) > 1:
            result[-2] = result[-1] * 1000 + result[-2]
            result.pop()

        return [num for num in reversed(result)]

    def parse_roman_groups(self, roman: str) -> list[tuple[str, int]]:
        if self.THOUSAND_INDICATOR not in roman:
            return [(roman, 0)]

        groups = roman.split(self.THOUSAND_INDICATOR)
        result = []

        for group in groups:
            if group:
                result.append((group, 1))
            else:
                if not result:
                    raise exc.InvalidRomanNumeralError(
                        "Formato de número romano extendido inválido"
                    )
                last_group, count = result.pop()
                result.append((last_group, count + 1))

        if result:
            last_group, count = result.pop()
            result.append((last_group, count - 1))

        return result

    def validate_extended_roman(self, roman: str) -> None:
        special_chars = set((" ", "\t", "\n"))
        allowed_chars = (
            set(ROMAN_TO_ARABIC_MAP.keys()) | {self.THOUSAND_INDICATOR} | special_chars
        )

        invalid_chars = set(roman) - allowed_chars
        if invalid_chars:
            raise exc.InvalidRomanNumeralError(f"Caracteres inválidos: {invalid_chars}")

        roman = roman.upper().strip()

        if not roman:
            raise exc.InvalidRomanNumeralError("Cadena romana vacía.")

    def to_roman(self, number: int) -> str:
        if number <= values.MAX_STANDARD_ROMAN.value:
            return self._standard_converter.to_roman(number)

        groups = self.split_into_thousands(number)
        levels = len(groups)
        result = ""

        for index, group in enumerate(groups):
            if group == 0:
                continue

            partial_roman = self._standard_converter.to_roman(group)
            level_suffix = self.THOUSAND_INDICATOR * (levels - index - 1)
            result += partial_roman + level_suffix

        return result

    def to_arabic(self, roman: str) -> int:
        self.validate_extended_roman(roman)

        try:
            groups = self.parse_roman_groups(roman)
        except Exception as e:
            raise exc.InvalidRomanNumeralError(f"Error al procesar número romano: {e}")

        result = 0

        for roman_part, exponent in groups:
            if not roman_part:
                continue

            try:
                partial_arabic = self._standard_converter.to_arabic(roman_part)
                result += partial_arabic * (1000**exponent)
            except Exception as e:
                raise exc.InvalidRomanNumeralError(f"Error en conversión: {e}")

        return result


class RomanCalculator(IRomanCalculator):
    def __init__(self) -> None:
        self._standard_converter = StandardRomanConverter(ARABIC_TO_ROMAN_MAP)
        self._extended_converter = ExtendedRomanProcessor(self._standard_converter)

    def to_roman(self, number: int) -> str:
        validate_number = RomanNumeralValidator.validate_arabic_input(number)
        return self._extended_converter.to_roman(validate_number)

    def to_arabic(self, roman: str) -> int:
        validate_roman = RomanNumeralValidator.validate_roman_input(roman)
        return self._extended_converter.to_arabic(validate_roman)


def create_roman_calculator() -> RomanCalculator:
    return RomanCalculator()
