import re

from src.utils import roman_exceptions as exc


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
