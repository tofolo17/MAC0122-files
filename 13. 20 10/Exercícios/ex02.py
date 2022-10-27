def fibonacciI(n):
    if n == 0: return 0
    anterior, atual = 0, 1
    for i in range(1, n):
        anterior, atual = atual, atual + anterior
    return atual


def fibonacciR(n):
    if n <= 1: return n
    return fibonacciR(n - 1) + fibonacciR(n - 2)


print(fibonacciI(-1))
print(fibonacciR(-2))

# c, e, h, j, k, m, n, p
# o, l == q (?)
