numbers = range(2, 21, 2)
iterator = iter(numbers)

for _ in numbers:
    print(next(iterator))
