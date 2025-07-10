ROMAN_NUMERAL_PAIRS = {
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

ROMAN_TO_INT = {symbol: value for value, symbol in ROMAN_NUMERAL_PAIRS.items()}


def is_valid_roman(roman: str) -> bool:
    import re

    roman_pattern = re.compile(
        "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    )
    return bool(roman_pattern.fullmatch(roman.upper()))


def from_arabic_to_roman(number: int) -> str:
    if not 1 <= number < 4000:
        raise ValueError("El número tiene que estar entre 0 y 3999.")

    result = []

    for value, numeral in ROMAN_NUMERAL_PAIRS.items():
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
