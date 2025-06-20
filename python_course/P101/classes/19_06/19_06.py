import pytest


def successive_differences(list_numbers: list[int]) -> list[int]:
    result = []
    for number in range(len(list_numbers) - 1):
        subtraction = list_numbers[number + 1] - list_numbers[number]
        result.append(subtraction)
    return result


class TestSuccessiveDifferences:
    @pytest.mark.parametrize(
        "input_list, expected_output",
        [
            ([72, 72, 75, 75, 70, 74, 74, 76], [0, 3, 0, -5, 4, 0, 2]),
            ([1, 2, 3], [1, 1]),
            ([10], []),
            ([5, 5], [0]),
            ([100, 200, 300], [100, 100]),
        ],
    )
    def test_successive_differences_with_params(
        self, input_list: list[int], expected_output: list[int]
    ) -> None:
        assert successive_differences(input_list) == expected_output

    def test_successive_differences_without_params(self) -> None:
        assert successive_differences([]) == []


if __name__ == "__main__":
    list_numbers = [72, 72, 75, 75, 70, 74, 74, 76]

    print(successive_differences(list_numbers))
