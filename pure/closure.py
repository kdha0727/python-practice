def make_odd_calculator():
    a = 2
    b = 1

    def inner(x):
        return a * x - b
    return inner
    # return lambda x: a * x + b


def make_accumulator():
    total = 0

    def inner(x):
        nonlocal total
        total = total + x
        print(total)
    return inner


calc = make_accumulator()
calc(1)
calc(2)
calc(3)
print(calc.__closure__[0].cell_contents)
