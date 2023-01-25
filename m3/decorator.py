def divide_decorator(func):
    def divide_inner(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Nolga bo'lish mumkin emas!"

    return divide_inner


def increment_arg_if_second_zero(func):
    def inner(a, b):
        if b == 0:
            b += 1
        return func(a, b)

    return inner


@divide_decorator
@increment_arg_if_second_zero
def divider(a, b):
    return a / b


print(divider(10, 5))
print(divider(10, 0))
