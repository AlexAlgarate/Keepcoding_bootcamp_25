from dataclasses import dataclass


@dataclass(frozen=True)
class AgeCategory:
    name: str
    min_age: int | None
    max_age: int | None
    price: int
    label: str


def contains_age(age: int, category: AgeCategory) -> bool:
    min_age_valid = category.min_age is None or age >= category.min_age
    max_age_valid = category.max_age is None or age <= category.max_age

    return min_age_valid and max_age_valid


def categorize_age(age: int, categories: list[AgeCategory]) -> AgeCategory | None:
    return next(
        (category for category in categories if contains_age(age, category)), None
    )


def get_visitor_age() -> int | None:
    ticket = input("Edad del visitante: ").strip()

    if ticket == "":
        return None

    if not ticket.isdigit():
        print("Debes introducir un número entero positivo.")
        return -1

    age = int(ticket)
    if age < 0:
        print("❌ La edad no puede ser negativa. Intenta de nuevo.")
        return -1

    return age


def calculate_total_price(
    counter: dict[str, int], categories: list[AgeCategory]
) -> int:
    return sum([counter[category.name] * category.price for category in categories])


def print_detailed_price(
    counter: dict[str, int], categories: list[AgeCategory]
) -> None:
    print("\n- Detalle por edades:")
    for category in categories:
        quantity = counter[category.name]
        if quantity > 0:
            subtotal = quantity * category.price
            print(f"\t {category.label}: {quantity} x {category.price} = {subtotal} €")


def main() -> None:
    CATEGORIES = [
        AgeCategory(
            name="BABIES",
            min_age=None,
            max_age=2,
            price=0,
            label="Bebés (0-2 años)",
        ),
        AgeCategory(
            name="KIDS",
            min_age=3,
            max_age=12,
            price=14,
            label="Niños (3-12 años)",
        ),
        AgeCategory(
            name="ADULTS",
            min_age=13,
            max_age=64,
            price=23,
            label="Adultos (13-64 años)",
        ),
        AgeCategory(
            name="RETIRED",
            min_age=65,
            max_age=None,
            price=18,
            label="Jubilados (+65 años)",
        ),
    ]
    print(
        "\nIntroduce la edad de cada visitante. Pulsa ENTER sin escribir nada para terminar.\n"
    )

    counter = {category.name: 0 for category in CATEGORIES}

    while True:
        age = get_visitor_age()

        if age is None:
            print("\n---\tSaliendo del programa\t---")
            break
        elif age == -1:
            continue

        category = categorize_age(age, CATEGORIES)
        if category:
            counter[category.name] += 1

    total = calculate_total_price(counter, CATEGORIES)
    print(f"\nPrecio total del grupo: {total} €")
    print_detailed_price(counter, CATEGORIES)


if __name__ == "__main__":
    main()
