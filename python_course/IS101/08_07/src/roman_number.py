from __future__ import annotations

from typing import Any

from src.converters.roman_converter import RomanConverter


class RomanNumber:
    def __init__(self, value: str | int) -> None:
        self._converter = RomanConverter()
        if isinstance(value, str):
            self.roman_string = value
            self.arabic_number = self._converter._extended_converter.to_arabic(value)
        else:
            self.arabic_number = value
            self.roman_string = self._converter._extended_converter.to_roman(value)

    def __repr__(self) -> str:
        return self.roman_string

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other) -> bool:
        if isinstance(other, RomanNumber):
            return self.arabic_number == other.arabic_number

        return False

    def __hash__(self) -> int:
        return hash((self.arabic_number, self.roman_string))

    def __add__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            valor_de_la_suma = self.arabic_number + other

        elif isinstance(other, RomanNumber):
            valor_de_la_suma = self.arabic_number + other.arabic_number

        else:
            return NotImplemented

        return RomanNumber(valor_de_la_suma)

    def __radd__(self, other: int | RomanNumber) -> RomanNumber | Any:
        return self.__add__(other)

    def __sub__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic_number - other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic_number - other.arabic_number

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rsub__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other - self.arabic_number)
        else:
            return NotImplemented

    def __mul__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic_number * other
        elif isinstance(other, RomanNumber):
            resultado = self.arabic_number * other.arabic_number
        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rmul__(self, other: int | RomanNumber) -> RomanNumber | Any:
        return self.__mul__(other)

    def __truediv__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic_number // other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic_number // other.arabic_number

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rtruediv__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other // self.arabic_number)

        else:
            return NotImplemented

    def __mod__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic_number % other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic_number % other.arabic_number

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rmod__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other % self.arabic_number)

        else:
            return NotImplemented

    def __pow__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic_number**other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic_number**other.arabic_number

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rpow__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other**self.arabic_number)

        else:
            return NotImplemented
