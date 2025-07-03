from random import randint


def crear_baraja():
    palos = ["O", "C", "E", "B"]
    numeros = [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "S",
        "C",
        "R",
    ]
    return [numero + palo for palo in palos for numero in numeros]


def barajar(baraja):
    for pos in range(len(baraja)):
        nueva_pos = randint(0, len(baraja) - 1)
        baraja[pos], baraja[nueva_pos] = baraja[nueva_pos], baraja[pos]


baraja = crear_baraja()
print(baraja)
barajar(baraja)
print(baraja)
