fibCache = [0] * 200


def fib(num):
    if num <= 1:
        fibCache[num] = 1
    if fibCache[num] == 0:
        fibCache[num] = fib(num - 1) + fib(num - 2)

    return fibCache[num]


print(fib(100))
