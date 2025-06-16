def get_pair_number():
    for i in range(0, 1000, 2):
        yield i


iterator = get_pair_number()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
