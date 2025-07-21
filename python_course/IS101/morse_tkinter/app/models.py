from abc import ABC, abstractmethod

char_to_morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


morse_to_char_dict = {k: v for v, k in char_to_morse_dict.items()}


class IMorseConverter(ABC):
    @abstractmethod
    def text_to_morse(self, text: str) -> str:
        pass

    @abstractmethod
    def morse_to_text(self, morse: str) -> str:
        pass


class MorseConverter:
    WHITE_SPACE_WORDS = "   "
    WHITE_SPACE_LETTERS = " "

    def text_to_morse(self, text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Debe insertar un texto válido.")

        return self.WHITE_SPACE_WORDS.join(
            self.WHITE_SPACE_LETTERS.join(
                char_to_morse_dict[letter]
                for letter in word
                if letter in char_to_morse_dict
            )
            for word in text.upper().split()
        )

    def morse_to_text(self, morse: str) -> str:
        words = morse.strip().split(self.WHITE_SPACE_WORDS)
        decoded_words = [
            "".join(
                morse_to_char_dict.get(letter, "")
                for letter in word.split(self.WHITE_SPACE_LETTERS)
            )
            for word in words
        ]
        return " ".join(decoded_words).capitalize()


# def text_to_morse(text: str):
#     words = text.upper().split()
#     morse_words = []

#     for word in words:
#         morse_letters = []
#         for letter in word:
#             if letter in char_to_morse_dict:
#                 morse_letters.append(char_to_morse_dict[letter])
#         morse_word = " ".join(morse_letters)
#         morse_words.append(morse_word)

#     return "   ".join(morse_words)

converter = MorseConverter()
hola_mundo_to_morse = converter.text_to_morse("hola mundo")
print(f"hola_mundo en morse: {hola_mundo_to_morse}")


decoded_morse = converter.morse_to_text(hola_mundo_to_morse)
print(f"Decoded morse: {decoded_morse}")
