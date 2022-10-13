# número de espaços usados para indicar a hereditariedade das chamadas
TAB = '    '  # 4 espaços


def main():
    print("Teste fatorialRX():")
    k = fatorialRX(3)
    print(f"fatorialRX(3) = {k}\n")

    print("Teste conte_collatz():")
    k = conte_collatz(7)
    print(f"\nconte_collatz(7) = {k}\n")

    print("Teste HanoiA():")
    k = hanoiA(4, 'A', 'B', 'C')
    print(f"hanoiA(4,'A','B','C') = {k}\n")

    print("Teste HanoiB():")
    k = hanoiB(4, 'A', 'B', 'C')
    print(f"hanoiB(4,'A','B','C') = {k}\n")

    print("Teste HanoiC():")
    k = hanoiC(3, 'A', 'B', 'C')
    print(f"hanoiC(3,'A','B','C') = {k}")


# ---------------------------------------------------------------------
def fatorialRX(n, level=0):
    if n == 0:
        print(TAB * level + f"fatorialRX({n}) = {1}")
        return 1
    else:
        print(TAB * level + f"fatorialRX({n})")
        result = fatorialRX(n - 1, level + 1) * n
        print(TAB * level + f"fatorialRX({n}) = {result}")
        return result


# ---------------------------------------------------------------------
def collatz(n, level=0):
    print(f"{n} ", end="")
    # caso base
    if n == 1:
        return level
    # simplifique?
    if n % 2 == 0:
        return collatz(n // 2, level + 1)
    else:
        return collatz(3 * n + 1, level + 1)


def conte_collatz(n):
    return collatz(n)


# ---------------------------------------------------------------------
def hanoiA(n, origem, auxiliar, destino):
    if n == 0:
        return 0
    a = hanoiA(n - 1, origem, destino, auxiliar)
    print(f"mova o disco {n} do pino {origem} para o pino {destino}")
    b = hanoiA(n - 1, auxiliar, origem, destino)
    return a + b + 1


# ---------------------------------------------------------------------
def hanoiB(n, origem, auxiliar, destino, mov=0):
    if n == 0:
        return mov
    mov = hanoiB(n - 1, origem, destino, auxiliar, mov)

    # Quantos movimentos foram feitos até agora, mais 1.
    print(f"{mov + 1}: mova o disco {n} do pino {origem} para o pino {destino}")
    return hanoiB(n - 1, auxiliar, origem, destino, mov + 1)


# ---------------------------------------------------------------------
def hanoiC(n, origem, auxiliar, destino, mov=0, level=0):
    print(TAB * level + f"hanoi({n},'{origem}','{auxiliar}','{destino}')")
    if n == 0:
        return mov

    mov = hanoiC(n - 1, origem, destino, auxiliar, mov, level + 1)

    print(TAB * (level + 1) + f"hanoi({n - 1},'{origem}','{destino}','{auxiliar}') = {2 ** (n - 1) - 1}")
    print(TAB * (level + 1) + f"{mov + 1}: mova o disco {n} do pino {origem} para o pino {destino}")

    mov = hanoiC(n - 1, auxiliar, origem, destino, mov + 1, level + 1)
    print(TAB * (level + 1) + f"hanoi({n - 1},'{auxiliar}','{origem}','{destino}') = {2 ** (n - 1) - 1}")

    return mov


if __name__ == "__main__":
    main()
