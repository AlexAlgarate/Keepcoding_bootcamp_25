"""
Fizz si el numero es divisible entre 3
"""

n = int(input("Introduce un numero: "))
fizz = lambda x: "Fizz" if x % 3 == 0 else x
print(fizz(n))

"""
FizzBuzz si el numero es divisible entre 15, etc.
"""

fizzbuzz = (
    lambda x: "FizzBuzz"
    if x % 15 == 0
    else ("Fizz" if x % 3 == 0 else ("Buzz" if x % 5 == 0 else x))
)
