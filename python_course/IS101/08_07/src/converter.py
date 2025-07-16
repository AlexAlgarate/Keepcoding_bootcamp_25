import re
from types import MappingProxyType

from . import roman_exceptions as exc
from .roman_number_interface import IRomanCalculator

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


class RomanNumeralValidator:
    _ROMAN_REGEX = re.compile(
        "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    )

    @classmethod
    def is_valid_roman(cls, roman: str) -> bool:
        return bool(cls._ROMAN_REGEX.fullmatch(roman.upper()))

    @classmethod
    def validate_arabic_input(cls, number: int | float) -> int:
        if not isinstance(number, (int, float)):
            raise exc.NumberOutOfRangeError("El número debe ser numérico")

        if isinstance(number, float):
            if not number.is_integer():
                raise exc.NumberOutOfRangeError("El número debe ser entero")
            number = int(number)

        if number < 1:
            raise exc.NumberOutOfRangeError(
                f"El número debe ser mayor a 0. Recibido: {number}"
            )

        return number

    @classmethod
    def validate_roman_input(cls, roman: str) -> str:
        if not isinstance(roman, str):
            raise exc.InvalidRomanNumeralError("El valor debe ser una cadena de texto")

        roman = roman.upper().strip()

        if not roman:
            raise exc.InvalidRomanNumeralError("Cadena romana vacía.")

        return roman


class StandardRomanConverter(IRomanCalculator):
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
        if number <= StandardRomanConverter.MAX_STANDARD_ROMAN:
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
