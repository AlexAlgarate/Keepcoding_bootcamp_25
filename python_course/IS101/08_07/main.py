from src.converters.roman_converter import create_roman_calculator
from src.roman_number import RomanNumber

if __name__ == "__main__":
    calculator = create_roman_calculator()

    print(calculator.to_roman(1500))

    print(RomanNumber(2**3))
