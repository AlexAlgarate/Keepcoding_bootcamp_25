def de_arabigo_a_romano(n: int) -> str:
    componentes = split_number(n)  # [1000, 900, 70, 6]

    resultado = ""
    for n in componentes:
        for clave, valor in dict_roman_numbers.items():
            if valor == n:
                resultado += clave

    return resultado


def split_number(number: int) -> list[int]:
    list_divisors = [1000, 100, 10, 1]
    result = []

    for divisor in list_divisors:
        value = (number // divisor) * divisor

        result.append(value)
        number %= divisor
    return result


def build_tens(number: int, roman_numbers: dict[str, int]) -> str:
    result = ""
    tens_of_number = split_number(number)[-2]
    print(f"tens_of_number -->  {tens_of_number}")
    aux = []
    for key, value in roman_numbers.items():
        if tens_of_number >= value:
            # print(f"AUX contains --> {key, value}")

            aux.append((key, value))

    target_key = aux[-1]
    letter = target_key[0]
    repetitions = tens_of_number // target_key[1]

    result += repetitions * letter
    return result


def int_to_roman(number: int, roman_numeral_dict: dict[str, int]) -> str:
    if number <= 0:
        raise ValueError("No existen números romanos para valores ≤ 0.")
    if number >= 4000:
        raise ValueError("Los números romanos tradicionales llegan hasta 3999.")

    result = ""

    sorted_dict = sorted(roman_numeral_dict.items(), key=lambda x: x[1], reverse=True)
    for numeral, value in sorted_dict:
        while number >= value:
            result += numeral
            number -= value
    return result


dict_roman_numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
# tens = build_tens(2530, dict_roman_numbers)
# print(tens)

roman_numeral_dict = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}
print(int_to_roman(1054, roman_numeral_dict))
