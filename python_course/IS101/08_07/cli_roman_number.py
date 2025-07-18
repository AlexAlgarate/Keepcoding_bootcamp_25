from src.calculatum_cli.application import calculate_operation
from src.calculatum_cli.infrastructure import (
    continue_or_exit,
    input_number,
    input_operation,
    show_available_operations,
)


def main() -> None:
    while True:
        number_one = input_number("Introduzca el primer número: ")
        number_two = input_number("Introduzca el segundo número: ")

        operation_options = show_available_operations()

        operation = input_operation(f"Operación ({operation_options}): ")

        result = calculate_operation(number_one, number_two, operation)
        print(f"Resultado: {number_one} {operation.value} {number_two} = {result}")

        if not continue_or_exit("¿Quiere hacer otro cálculo (s/n)?"):
            break

    print("Hasta luego")


if __name__ == "__main__":
    main()
