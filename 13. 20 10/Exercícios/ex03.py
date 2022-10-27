def fibonacciRM(n):
    cache = [-1] * (n + 1)
    return fibonacciRCache(n, cache)


def fibonacciRCache(n, cache):
    if cache[n] > -1:
        return cache[n]
    elif n < 2:
        cache[n] = n
    else:
        cache[n - 1] = fibonacciRCache(n - 1, cache)
        cache[n - 2] = fibonacciRCache(n - 2, cache)
        cache[n] = cache[n - 1] + cache[n - 2]
    return cache[n]


print(fibonacciRM(1))
# b, c, d, f, i, k, n
