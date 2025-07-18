from src.constants.constants import ROMAN_TO_ARABIC_MAP
from src.constants.constants import MinMaxValues as values

from .converter_interface import IRomanCalculator
from .standard_converter import StandardRomanConverter


class ExtendedRomanConverter(IRomanCalculator):
    THOUSAND_INDICATOR = "•"

    def __init__(self, standard_converter: StandardRomanConverter):
        self._standard_converter = standard_converter

    def _split_into_thousands(self, number: int) -> list[int]:
        if number == 0:
            return [0]

        groups = []

        while number > 0:
            resto = number % 1000
            groups.append(resto)
            number //= 1000

        # Combina el grupo más significativo si es menor que 4 y hay más de un grupo
        if groups[-1] < 4 and len(groups) > 1:
            groups[-2] += groups[-1] * 1000
            groups.pop()

        return list(reversed(groups))

    def _parse_roman_groups(self, roman: str) -> list[tuple[str, int]]:
        if self.THOUSAND_INDICATOR not in roman:
            return [(roman, 0)]

        groups = roman.split(self.THOUSAND_INDICATOR)

        parsed = []

        for group in groups:
            if group:
                parsed.append((group, 1))

            else:
                if not parsed:
                    raise ValueError("Formato de número romano extendido inválido")
                last_group, count = parsed.pop()
                parsed.append((last_group, count + 1))

        # El último grupo tiene un punto extra que hay que eliminar
        if parsed:
            last_group, count = parsed.pop()
            parsed.append((last_group, count - 1))

        return parsed

    def _validate_extended_roman(self, roman: str) -> None:
        roman = roman.upper().strip()

        if not roman:
            raise ValueError("Cadena romana vacía.")

        special_chars = set((" ", "\t", "\n"))
        allowed_chars = (
            set(ROMAN_TO_ARABIC_MAP) | {self.THOUSAND_INDICATOR} | special_chars
        )
        invalid_chars = set(roman) - allowed_chars

        if invalid_chars:
            raise ValueError(f"Caracteres inválidos: {invalid_chars}")

    def to_roman(self, number: int) -> str:
        if number <= values.MAX_STANDARD_ROMAN.value:
            return self._standard_converter.to_roman(number)

        groups = self._split_into_thousands(number)
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
        self._validate_extended_roman(roman)

        try:
            groups = self._parse_roman_groups(roman)
        except Exception as e:
            raise ValueError(f"Error al procesar número romano: {e}")

        result = 0

        for roman_part, exponent in groups:
            if not roman_part:
                continue

            try:
                partial_arabic = self._standard_converter.to_arabic(roman_part)
                result += partial_arabic * (1000**exponent)
            except Exception as e:
                raise ValueError(f"Error en conversión: {e}")

        return result
