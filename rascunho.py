def fibonacciR(n, nos=0):
    if n == 0:
        return 0, nos
    if n == 1:
        return 1, nos

    a, nos = fibonacciR(n - 1, nos)
    b, nos = fibonacciR(n - 2, nos + 1)

    return a + b, nos


def nos_fibo(n):
    return fibonacciR(n)[1] - 1


nos_fibo(5)
