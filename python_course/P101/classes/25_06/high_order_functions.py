"""
FILTER
MAP
REDUCE
"""

from functools import reduce


def add_1(list_numbers: list) -> list[int]:
    new_list = []
    for number in list_numbers:
        new_list.append(number + 1)
    return new_list


def square(list_numbers: list) -> list[int]:
    new_list = []
    for number in list_numbers:
        new_list.append(number**2)
    return new_list


def sum_all_numbers(list_numbers: list) -> int:
    return sum(list_numbers)


def filter_list_numbers(list_numbers: list) -> list[int]:
    result = []
    for number in list_numbers:
        if number % 2 == 0:
            result.append(number)
    return result


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("add_1 without high order function -->", add_1(list_numbers))
print("add_1 USING MAP -->", list(map(lambda x: x + 1, list_numbers)), "\n")

print("square without high order function -->", square(list_numbers))
print("square USING MAP-->", list(map(lambda x: x**2, list_numbers)), "\n")

print("Sum all numbers from a list --> ", sum_all_numbers(list_numbers))
print(
    "Sum all numbers from a list using REDUCE --> ",
    reduce(lambda x, y: x + y, list_numbers),
    "\n",
)


print(
    "Using a function that filters numbers without high order function -->",
    filter_list_numbers(list_numbers),
)
print(
    "Filter numbers using FILTER -->",
    list(filter(lambda x: x % 2 == 0, list_numbers)),
    "\n",
)
