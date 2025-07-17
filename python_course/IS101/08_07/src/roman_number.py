from __future__ import annotations

from typing import Any

from src.converters.roman_converter import RomanConverter


class RomanNumber:
    def __init__(self, value: str | int) -> None:
        self._converter = RomanConverter()
        if isinstance(value, str):
            self.roman = value
            self.arabic = self._converter._extended_converter.to_arabic(value)
        else:
            self.arabic = value
            self.roman = self._converter._extended_converter.to_roman(value)

    def __repr__(self) -> str:
        return self.roman

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other) -> bool:
        if isinstance(other, RomanNumber):
            return self.arabic == other.arabic

        return False

    def __hash__(self) -> int:
        return hash((self.arabic, self.roman))

    def __add__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            valor_de_la_suma = self.arabic + other

        elif isinstance(other, RomanNumber):
            valor_de_la_suma = self.arabic + other.arabic

        else:
            return NotImplemented

        return RomanNumber(valor_de_la_suma)

    def __radd__(self, other: int | RomanNumber) -> RomanNumber | Any:
        return self.__add__(other)

    def __sub__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic - other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic - other.arabic

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rsub__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other - self.arabic)
        else:
            return NotImplemented

    def __mul__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic * other
        elif isinstance(other, RomanNumber):
            resultado = self.arabic * other.arabic
        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rmul__(self, other: int | RomanNumber) -> RomanNumber | Any:
        return self.__mul__(other)

    def __truediv__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic // other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic // other.arabic

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rtruediv__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other // self.arabic)

        else:
            return NotImplemented

    def __mod__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic % other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic % other.arabic

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rmod__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other % self.arabic)

        else:
            return NotImplemented

    def __pow__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            resultado = self.arabic**other

        elif isinstance(other, RomanNumber):
            resultado = self.arabic**other.arabic

        else:
            return NotImplemented

        return RomanNumber(resultado)

    def __rpow__(self, other: int | RomanNumber) -> RomanNumber | Any:
        if isinstance(other, int):
            return RomanNumber(other**self.arabic)

        else:
            return NotImplemented
