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


def text_to_morse(text: str):
    WHITE_SPACE_WORDS = "   "
    WHITE_SPACE_LETTERS = " "

    return WHITE_SPACE_WORDS.join(
        WHITE_SPACE_LETTERS.join(
            char_to_morse_dict[letter]
            for letter in word
            if letter in char_to_morse_dict
        )
        for word in text.upper().split()
    )


def morse_to_text(morse: str):
    WHITE_SPACE_WORDS = "   "
    WHITE_SPACE_LETTERS = " "

    words = morse.strip().split(WHITE_SPACE_WORDS)

    decoded_words = []

    for word in words:
        letters = word.split(WHITE_SPACE_LETTERS)
        decoded_letters = [morse_to_char_dict.get(letter, "") for letter in letters]
        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)


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


hola_mundo_to_morse = text_to_morse("hola mundo")
print(f"hola_mundo en morse: {hola_mundo_to_morse}")


decoded_morse = morse_to_text(hola_mundo_to_morse)
print(f"Decoded morse: {decoded_morse}")
