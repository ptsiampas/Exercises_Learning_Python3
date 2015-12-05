# new Fib function, pretty cool

alreadyknown = {0: 0, 1: 1}


def fib(n):
    if n not in alreadyknown:
        new_value = fib(n - 1) + fib(n - 2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


print(fib(200))
