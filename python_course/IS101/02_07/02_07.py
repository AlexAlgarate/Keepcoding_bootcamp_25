"""

Ejercicio: Creador de clickers con funciones de orden superior

Tu objetivo es crear una función llamada creador_de_clickers() que genere clickers. Un clicker es una función que, cada vez que se invoca, devuelve un número que aumenta secuencialmente.

Parte 1
Define la función creador_de_clickers() de forma que, al invocarla, devuelva una nueva función. Esa función interna (que podrás asignar a cualquier nombre, por ejemplo mi_clicker) debe comportarse así:

La primera vez que se llama, devuelve 1.
La segunda vez, 2.
Y así sucesivamente: 3, 4, 5…

Cada clicker debe tener su propio contador independiente.

Parte 2
Amplía el comportamiento anterior para que el clicker admita un argumento opcional. Si se llama con el argumento "reset", debe reiniciar su contador a cero.
"""


def clicker_creator():
    counter = 0

    def clicker(arg: str | None = None) -> int:
        nonlocal counter

        if arg == "reset":
            counter = 0
            return 0

        counter += 1
        return counter

    return clicker


mi_clicker = clicker_creator()
# print(mi_clicker())
# print(mi_clicker())
# print(mi_clicker("reset"))
# print(mi_clicker())


class Day:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.validate_date()

    def validate_date(self):
        if not (1 <= self.day <= 31):
            raise ValueError("El día debe estar entre 1 y 31.")
        if not (1 <= self.month <= 12):
            raise ValueError("El mes debe estar entre 1 y 12.")


day = Day(5, 5, 2025)
# print(day.day, day.month, day.year)


class DNI:
    LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

    def __init__(self, number: str, letter: str) -> None:
        self.number = number
        self.letter = letter.upper()
        self._number_validator()
        self._letter_validator()

    def _number_validator(self) -> None:
        if len(self.number) != 8 or not self.number.isdigit():
            raise ValueError(
                "El número tiene que ser de 8 cifras y no puede contener letras."
            )

    def _letter_validator(self) -> None:
        if self.letter not in self.LETTERS:
            raise ValueError(f"La letra del DNI `{self.letter}` es inválida.")

        if not self.LETTERS[int(self.number) % 23] == self.letter:
            raise ValueError(
                "La letra no coincide con el número. Por favor, inserte una letra válida."
            )


dni_Alex_correcto = DNI("03175669", "J")  # OK
print(f"El número del DNI es --> {dni_Alex_correcto.number}")  # --> 03175669
print(f"La letra del DNI es --> {dni_Alex_correcto.letter}")  # --> J
# dni_Alex_incorrecto = DNI("03175669", "A")  # ValueError


class DNIProperties:
    LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

    def __init__(self, number: str, letter: str) -> None:
        self.number = number
        self.letter = letter.upper()
        self.validate_dni()

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, value: str) -> None:
        if len(value) != 8 or not value.isdigit():
            raise ValueError(
                "El número tiene que tener de 8 cifras y no puede contener letras."
            )
        self._number = value

    @property
    def letter(self) -> str:
        return self._letter

    @letter.setter
    def letter(self, value: str) -> None:
        if value not in self.LETTERS:
            raise ValueError(f"La letra del DNI `{value}` es inválida.")

        self._letter = value.upper()

    def validate_dni(self) -> str:
        expected_letter = self.LETTERS[int(self._number) % 23]
        if self._letter != expected_letter:
            raise ValueError(
                f"La letra {self._letter} no coincide con el número {self._number}. Por favor, inserte una letra válida."
            )

        return "OOOOK"


dni_Alex_correcto_properties = DNIProperties("03175669", "J")  # OK
print(f"El número del DNI es --> {dni_Alex_correcto_properties.number}")  # --> 03175669
print(f"La letra del DNI es --> {dni_Alex_correcto_properties.letter}")  # --> J
