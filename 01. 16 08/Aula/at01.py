"""
    Atividade 01 - funções em Python

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: S

    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Vicenzo Carlim de Sousa
    - Gustavo Valencio Tofolo
    - Rennisson Davi Domingos Alves

"""


def main():
    """
    Programa que testa as funções.
    """
    print("Testes fat()\n")

    print("Teste n=0")
    print(f"fat(0) = {fat(0)} e deve ser 1\n")

    print("Teste n=1")
    print(f"fat(1) = {fat(1)} e deve ser 1\n")

    print("Teste n=2")
    print(f"fat(2) = {fat(2)} e deve ser 2\n")

    print("Teste n=3")
    print(f"fat(3) = {fat(3)} e deve ser 6\n")

    print("Teste n=5")
    print(f"fat(5) = {fat(5)} e deve ser 120\n")

    print('-------------\n')

    print("Testes combinacao()\n")

    print("Teste m=3, n=0")
    print(f'combinacao(3, 0) = {combinacao(3, 0)} e deve ser 1\n')

    print("Teste m=2, n=2")
    print(f'combinacao(2, 2) = {combinacao(2, 2)} e deve ser 1\n')

    print("Teste m=1, n=2")
    print(f'combinacao(1, 2) = {combinacao(1, 2)} e deve ser -1 (erro)\n')

    print("Teste m=4, n=1")
    print(f'combinacao(4, 1) = {combinacao(4, 1)} e deve ser 4\n')

    print("Teste m=4, n=3")
    print(f'combinacao(4, 3) = {combinacao(4, 3)} e deve ser 4\n')

    print('-------------\n')

    print('Teste mdc_fb()\n')

    print("Teste m=4, n=4")
    print(f'mdc_fb(4, 4) = {mdc_fb(4, 4)} e deve ser igual a 4\n')

    print("Teste m=24, n=18")
    print(f'mdc_fb(24, 18) = {mdc_fb(24, 18)} e deve ser igual a 6\n')

    print("Teste m=150, n=120")
    print(f'mdc_fb(150, 120) = {mdc_fb(150, 120)} e deve ser igual a 30\n')

    print("Teste m=241, n=2513")
    print(f'mdc_fb(241, 2513) = {mdc_fb(241, 2513)} e deve ser igual a 1\n')

    print("Teste m=150, n=120")
    print(f'mdc_fb(150, 120) = {mdc_fb(150, 120)} e deve ser igual a 30\n')

    print("Teste m=150, n=1")
    print(f'mdc_fb(150, 1) = {mdc_fb(150, 1)} e deve ser igual a 1\n')

    print('-------------\n')

    print('Teste mdc()\n')

    print("Teste m=4, n=4")
    print(f'mdc(4, 4) = {mdc(4, 4)} e deve ser igual a 4\n')

    print("Teste m=24, n=18")
    print(f'mdc(24, 18) = {mdc(24, 18)} e deve ser igual a 6\n')

    print("Teste m=150, n=120")
    print(f'mdc(150, 120) = {mdc(150, 120)} e deve ser igual a 30\n')

    print("Teste m=241, n=2513")
    print(f'mdc(241, 2513) = {mdc(241, 2513)} e deve ser igual a 1\n')

    print("Teste m=150, n=120")
    print(f'mdc(150, 120) = {mdc(150, 120)} e deve ser igual a 30\n')

    print("Teste m=150, n=1")
    print(f'mdc(150, 1) = {mdc(150, 1)} e deve ser igual a 1\n')


# ----------------------------------------------------
def fat(n):
    """ (int) -> int

    Recebe um inteiro n e retorna n!
    Exemplos:
    >>> fat(0)
    1
    >>> fat(1)
    1
    >>> fat(3)
    6
    """
    resultado = 1
    i = 2
    while i <= n:
        resultado *= i
        i += 1
    return resultado


# ----------------------------------------------------
def combinacao(m, n):
    """(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    """
    if n > m:
        print("Entrada inválida (n deve ser menor que m).")
        return -1

    return fat(m) // (fat(m - n) * fat(n))


# ----------------------------------------------------
def mdc_fb(m, n):
    """
    (int, int) -> int
    """
    menor = 0
    if m > n:
        menor = n
    elif n > m:
        menor = m
    else:
        return m

    for i in range(menor, 0, -1):
        if m % i == 0 and n % i == 0:
            return i


# ----------------------------------------------------
def mdc(m, n):
    """
    (int, int) -> int
    """

    """
    resto = -1
    while resto != 0:
        resto = m % n
        if resto == 0:
            return n
        m = n
        n = resto
    """

    resto = m % n
    if resto == 0:
        return n
    return mdc(n, resto)


# ----------------------------------------------------
if __name__ == '__main__':
    main()
