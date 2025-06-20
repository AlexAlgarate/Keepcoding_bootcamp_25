from typing import Callable, Sequence

import pytest


def successive_differences_for(list_numbers: list[int]) -> list[int]:
    result = []
    for number in range(len(list_numbers) - 1):
        subtraction = list_numbers[number + 1] - list_numbers[number]
        result.append(subtraction)
    return result


def successive_differences_zip(list_numbers: list[int]) -> list[int]:
    return [b - a for a, b in zip(list_numbers, list_numbers[1:])]


def filter_growing_for(list_numbers: list[int]) -> list[int]:
    result = []
    for number in range(len(list_numbers) - 1):
        if list_numbers[number + 1] > list_numbers[number]:
            result.append(list_numbers[number + 1])
    return result


def filter_growing_zip(numbers: list[int]) -> list[int]:
    return [b for a, b in zip(numbers, numbers[1:]) if b > a]


class TestDifferences:
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
        assert successive_differences_for(input_list) == expected_output
        assert successive_differences_zip(input_list) == expected_output

    def test_successive_differences_without_params(self) -> None:
        assert successive_differences_for([]) == []
        assert successive_differences_zip([]) == []

    @pytest.mark.parametrize(
        "input_list, expected_output",
        [
            ([72, 72, 75, 75, 70, 74, 74, 76], [75, 74, 76]),
            ([1, 2, 2, 4, 5, 6], [2, 4, 5, 6]),
            ([10, 20, 30, 30, 20, 30], [20, 30, 30]),
            ([10], []),
        ],
    )
    def test_filter_growing_with_params(
        self, input_list: list[int], expected_output: list[int]
    ) -> None:
        assert filter_growing_for(input_list) == expected_output
        assert filter_growing_zip(input_list) == expected_output

    def test_filter_growing_without_params(self) -> None:
        assert filter_growing_for([]) == []
        assert filter_growing_zip([]) == []


if __name__ == "__main__":
    list_numbers = [72, 72, 75, 75, 70, 74, 74, 76]

    def print_function(func: Callable, iterable: Sequence) -> None:
        print(func(iterable))

    print_function(successive_differences_for, list_numbers)
    print_function(successive_differences_zip, list_numbers)
    print_function(filter_growing_for, list_numbers)
    print_function(filter_growing_zip, list_numbers)
