from src.roman_number import RomanNumber as RN


def input_number(message: str) -> RN:
    while True:
        user_input = input(message).strip()
        try:
            if user_input.isdigit():
                number = RN(int(user_input))
            else:
                number = RN(user_input.upper())
            return number
        except ValueError:
            print("Invalid Roman/integer number. Try again.")


def input_operation(message: str):
    pass


def continue_or_exit(message: str) -> bool:
    return input(message).strip().lower() == "s"
