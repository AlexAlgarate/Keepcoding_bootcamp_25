import random


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
        nueva_pos = random.randint(0, len(baraja) - 1)
        baraja[pos], baraja[nueva_pos] = baraja[nueva_pos], baraja[pos]


# baraja = crear_baraja()
# print(baraja)
# barajar(baraja)
# print(baraja)


class DeckCards:
    def __init__(self, suits: list[str], numbers: list[str]) -> None:
        self.suits = suits
        self.numbers = numbers
        self.deck = self.create_deck_of_cards()

    def create_deck_of_cards(self) -> list[str]:
        return [number + suit for suit in self.suits for number in self.numbers]

    def shuffle_cards_without_shuffle_method(self) -> None:
        for pos in range(len(self.deck)):
            new_pos = random.randint(0, len(self.deck) - 1)
            self.deck[pos], self.deck[new_pos] = (
                self.deck[new_pos],
                self.deck[pos],
            )

    def shuffle_cards(self):
        return random.shuffle(self.deck)

    def divide_up_cards(self, hand: int, players: int) -> list[list[str]]:
        total_cards = hand * players
        if total_cards > len(self.deck):
            raise ValueError(
                f"No hay suficientes cartas para repartir {hand} a {players} jugadores. Cartas restantes: {len(self.deck)}."
            )
        hands = [self.deck[i * hand : (i + 1) * hand] for i in range(players)]
        del self.deck[:total_cards]

        return hands


suits_sp = ["O", "C", "E", "B"]
numbers_sp = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]

deck_spain = DeckCards(suits=suits_sp, numbers=numbers_sp)
print(deck_spain.deck)
deck_spain.shuffle_cards()
print(f"\nShuffled cards --> {deck_spain.deck} \n")


print("Let's play!")
print(deck_spain.divide_up_cards(hand=4, players=9))


"""
Ejemplo con cartas de la baraja francesa.
suits_fr = ["♠", "♥", "♦", "♣"]
numbers_fr = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck_fr = DeckCards(suits=suits_fr, numbers=numbers_fr)
print(f"French deck --> {deck_fr.deck}\n")
deck_fr.shuffle_cards_without_shuffle_method()
print(f"Shuffled French deck --> {deck_fr.deck}\n")
deck_fr.shuffle_cards()
print(f"Shuffled French deck random.shuffle method--> {deck_fr.deck}\n")
"""
