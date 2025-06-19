MOBILE_KEYS = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " ",
}


def create_dictionary() -> dict:
    return {
        char: key * (i + 1)
        for key, chars in MOBILE_KEYS.items()
        for i, char in enumerate(chars)
    }


def message_to_keys(message: str) -> str:
    map = create_dictionary()
    return "".join([map[char] for char in message.upper() if char in map])


solution = "4433555555666110966677755531111"

sol_1 = message_to_keys("Hello, World!")
print(sol_1)
print(solution == sol_1)
