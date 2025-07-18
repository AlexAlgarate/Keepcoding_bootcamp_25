from src.calculatum_cli.infrastructure import continue_or_exit, input_number


def main() -> None:
    while True:
        number_one = input_number("Introduzca el primer número: ")
        number_two = input_number("Introduzca el segundo número: ")

        if not continue_or_exit("¿Quiere hacer otro cálculo (s/n)?"):
            break

        print(f"Number one: {number_one} || Number two: {number_two}")

    print(f"El resultado es: {number_one} || {number_two}")

    print("Hasta luego")


if __name__ == "__main__":
    main()
