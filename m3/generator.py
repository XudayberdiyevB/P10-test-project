# def generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# my_gen = generator()
#
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

def square(nums):
    for num in nums:
        yield num ** 2


numbers = [1, 2, 3]
generator = square(numbers)

print(next(generator))
print(next(generator))
print(next(generator))

