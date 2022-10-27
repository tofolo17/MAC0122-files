def indiceR(v, n, x):
    if n == 0:
        return None
    if v[n - 1] == x:
        return n - 1
    return indiceR(v, n - 1, x)


a = [1, 4, 3, 7, 8, 9]
print(indiceR(a, len(a), 1))

# a, b, g
