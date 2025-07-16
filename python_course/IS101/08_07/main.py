from src.roman_number import create_roman_calculator

if __name__ == "__main__":
    calculator = create_roman_calculator()

    print(calculator.to_roman(1500))
