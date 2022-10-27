def int2bin(n):
    if n == 0:
        return '0'
    if n // 2 != 0:
        return int2bin(n // 2) + str(n % 2)
    return str(n % 2)


int2bin(10)
