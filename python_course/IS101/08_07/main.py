import re
from abc import ABC, abstractmethod

ARABIC_TO_ROMAN_MAP = {
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

ROMAN_TO_INT = {symbol: value for value, symbol in ARABIC_TO_ROMAN_MAP.items()}


def is_valid_roman(roman: str) -> bool:
    roman_pattern = re.compile(
        "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    )
    return bool(roman_pattern.fullmatch(roman.upper()))


def from_arabic_to_roman(number: int) -> str:
    if not 1 <= number < 4000:
        raise ValueError("El número tiene que estar entre 0 y 3999.")

    result = []

    for value, numeral in ARABIC_TO_ROMAN_MAP.items():
        count, number = divmod(number, value)
        result.append(numeral * count)

    return "".join(result)


def from_roman_to_arabic(roman: str) -> int:
    if not is_valid_roman(roman):
        raise ValueError(f"Número romano no válido: '{roman}'")

    roman = roman.upper()
    result = 0
    previous = 0

    for char in reversed(roman):
        value = ROMAN_TO_INT[char]

        if char not in ROMAN_TO_INT:
            raise ValueError(f"Símbolo romano no permitido: {char}")

        if value < previous:
            result -= value
        else:
            result += value
            previous = value

    return result


class IRomanCalculator(ABC):
    @abstractmethod
    def from_arabic_to_roman(
        self, number: int, int_to_roman_map: dict[int, str]
    ) -> str:
        pass

    @abstractmethod
    def from_roman_to_arabic(
        self, roman_char: str, roman_to_int_map: dict[str, int]
    ) -> int:
        pass


class RomanCalculator(IRomanCalculator):
    @staticmethod
    def is_valid_roman(roman: str) -> bool:
        roman_pattern = re.compile(
            "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
        )
        return bool(roman_pattern.fullmatch(roman.upper()))

    def from_arabic_to_roman(
        self, number: int, int_to_roman_map: dict[int, str]
    ) -> str:
        if not 1 <= number <= 3999:
            raise ValueError(
                f"El número tiene que estar entre 1 y 3999. El recibido es {number}"
            )

        result = []

        for value, numeral in int_to_roman_map.items():
            count, number = divmod(number, value)

            if count:
                result.append(numeral * count)

        return "".join(result)

    def from_roman_to_arabic(self, roman: str, roman_to_int_map: dict[str, int]) -> int:
        roman = roman.upper().strip()

        if not roman:
            raise ValueError("Cadena romana vacía.")

        if not self.is_valid_roman(roman):
            raise ValueError(f"Número romano no válido: '{roman}'")

        result = 0
        previous = 0

        for char in reversed(roman):
            value = roman_to_int_map[char]

            if value < previous:
                result -= value
            else:
                result += value
                previous = value

        return result


def create_roman_calculator() -> RomanCalculator:
    return RomanCalculator()


if __name__ == "__main__":
    calculator = create_roman_calculator()

    number = 1234
    roman = "DCLXVI"

    print(
        f"From {number} to {calculator.from_arabic_to_roman(number, ARABIC_TO_ROMAN_MAP)}\n"
    )
    print(
        f"From {roman} to {calculator.from_roman_to_arabic(roman, ROMAN_TO_ARABIC_MAP)}\n"
    )
