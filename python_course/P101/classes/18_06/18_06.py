import pytest

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


def message_to_keys(message: str) -> str:
    map_dict = {
        char: key * (i + 1)
        for key, chars in MOBILE_KEYS.items()
        for i, char in enumerate(chars)
    }

    return "".join([map_dict[char] for char in message.upper() if char in map_dict])


solution = "0"

sol_1 = message_to_keys(" ")
print(sol_1)
print(solution == sol_1)


class TestMobile:
    @pytest.mark.parametrize(
        "input_text, expected_output",
        [
            ("Hello, World!", "4433555555666110966677755531111"),
            ("Python 3.10", "79998446666601"),
            ("KeepCoding", "55333372226663444664"),
            ("A B C", "20220222"),
            (" ", "0"),
        ],
    )
    def test_message_to_keys(self, input_text, expected_output):
        assert message_to_keys(input_text) == expected_output

    def test_message_to_keys_empty(self):
        assert message_to_keys("") == ""
