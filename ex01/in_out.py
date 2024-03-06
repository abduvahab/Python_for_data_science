def square(x: int | float) -> int | float:
    return x**2


def pow(x: int | float) -> int | float:
    return x**x


def outer(x: int | float, function) -> any:
    count = 0
    # count = x

    def inner() -> float:
        nonlocal count
        count += 1
        a = x
        for i in range(count):
            a = function(a)
        return a
    # count = x
    return inner
