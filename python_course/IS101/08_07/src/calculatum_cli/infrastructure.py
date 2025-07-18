from src.roman_number import RomanNumber as RN

from .domain import Operation


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


def input_operation(message: str) -> Operation:
    while True:
        user_input = input(message).strip()

        try:
            operation = Operation(user_input)
            break

        except ValueError:
            print("Invalid Roman/integer number. Try again.")

    return operation


def show_available_operations() -> str:
    symbols = [operation.value for operation in Operation]
    return ", ".join(symbols)


def continue_or_exit(message: str) -> bool:
    return input(message).strip().lower() == "s"
