"""
    Atividade 04 - classe Fraction

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: S

    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Gustavo Valencio Tofolo
    -Rennisson Davi D. Alves
    - Vicenzo Carlim de Sousa

"""


# ===================================================================


def main():
    """
        Programa main usado para teste da classe Fraction
        e pode ser usada também para testar as suas funções
        HFmaior e HFmenor, que devem usar obrigatoriamente a
        classe Fraction.

        Execute esse programa antes de escrever suas funções e
        estude a saída de cada teste da classe Fraction abaixo,
        lendo os comentários para entender o comportamento da classe
        antes de escrever suas funções HFmaior() e HFmenor().
    """

    # Criação de objetos do tipo Fraction
    frac23 = Fraction(2, 3)
    print(f"Fraction(2,3) = {frac23}")

    # chamada direta do método __str__() -- não fazemos isso normalmente!!
    print(f"frac23.__str__() = {frac23.__str__()}")
    # mas podemos usar o str() que chama o método __str__
    print(f"str(frac23) = {str(frac23)}")
    # e a função print() também chama o __str__ automaticamente
    # essas chamadas ficam "escondidas" para facilitar a leitura do código.
    print(f"frac23 = {frac23}")

    # Vamos criar mais algumas frações
    frac34 = Fraction(3, 4)
    print(f"frac34 = {frac34}")

    frac45 = Fraction(4, 5)
    print(f"frac45 = {frac45}")

    # chamada do método mul.
    # Observe a notação com . (ponto)
    print(f"frac34.mul(frac45) = {frac34.mul(frac45)}")

    # Declarando frações
    frac04 = Fraction(0, 4)
    frac48 = Fraction(4, 8)
    frac2311 = Fraction(23, 11)
    frac121 = Fraction(12, 1)

    # Coloque aqui mais testes de mul e dos demais operadores
    print('\nNossos testes')
    print('-' * 15, '\n')

    print('Testes multiplicação')
    print('-' * 15)
    print(f'{frac04} * {frac48} = {frac04.mul(frac48)}')
    print(f'{frac2311} * {frac121} = {frac2311.mul(frac121)}')
    print(f'{frac48} * {frac121} = {frac48.mul(frac121)}')
    print(f'{frac34} * {frac121} = {frac34.mul(frac121)}')
    print(f'{frac45} * {frac48} = {frac45.mul(frac48)}\n')

    print('Testes divisão')
    print('-' * 15)
    print(f'{frac04} / {frac48} = {frac04.div(frac48)}')
    print(f'{frac2311} / {frac121} = {frac2311.div(frac121)}')
    print(f'{frac48} / {frac121} = {frac48.div(frac121)}')
    print(f'{frac34} / {frac121} = {frac34.div(frac121)}')
    print(f'{frac45} / {frac48} = {frac45.div(frac48)}\n')

    print('Testes soma')
    print('-' * 15)
    print(f'{frac04} + {frac48} = {frac04.add(frac48)}')
    print(f'{frac2311} + {frac121} = {frac2311.add(frac121)}')
    print(f'{frac48} + {frac121} = {frac48.add(frac121)}')
    print(f'{frac34} + {frac121} = {frac34.add(frac121)}')
    print(f'{frac45} + {frac48} = {frac45.add(frac48)}\n')

    print('Testes subtração')
    print('-' * 15)
    print(f'{frac04} - {frac48} = {frac04.sub(frac48)}')
    print(f'{frac2311} - {frac121} = {frac2311.sub(frac121)}')
    print(f'{frac48} - {frac121} = {frac48.sub(frac121)}')
    print(f'{frac34} - {frac121} = {frac34.sub(frac121)}')
    print(f'{frac45} - {frac48} = {frac45.sub(frac48)}\n')

    # Coloque aqui os testes para as funções HFmaior e HFmenor
    print("\n::::::: Testes da função HFmenor :::::::\n")
    print("Série harmonica de ordem 2")
    print(f'Para n = 2: {HFmenor(2)}\n')

    print("Série harmonica de ordem 5")
    print(f'Para n = 5: {HFmenor(5)}\n')

    print("Série harmonica de ordem Pré-aula")
    print(f'Para n = Pré-aula: {HFmenor(10)}\n')

    print("Série harmonica de ordem 50")
    print(f'Para n = 50: {HFmenor(50)}\n')

    print("Série harmonica de ordem 100")
    print(f'Para n = 100: {HFmenor(100)}\n')

    print("\n::::::: Testes da função HFmaior :::::::\n")
    print("Série harmonica de ordem 2")
    print(f'Para n = 2: {HFmaior(2)}\n')

    print("Série harmonica de ordem 5")
    print(f'Para n = 5: {HFmaior(5)}\n')

    print("Série harmonica de ordem Pré-aula")
    print(f'Para n = Pré-aula: {HFmaior(10)}\n')

    print("Série harmonica de ordem 50")
    print(f'Para n = 50: {HFmaior(50)}\n')

    print("Série harmonica de ordem 100")
    print(f'Para n = 100: {HFmaior(100)}\n')

    # Gerando erros
    frac00 = Fraction(0, 0)
    print(frac00)


# ===================================================================
#  PARTE I: classe Fraction
# ===================================================================

class Fraction:
    """
        A classe Fraction representa uma fração.
        Uma fração é constituída por um numerador e um denominador,
        ambos inteiros, como por exemplo 2/5 (dois quintos),
        onde 2 é o numerador e 5 o denominador.
    """

    def __init__(self, n, d):
        """(Fraction, int, int) --> None

        Chamado pelo construtor da classe.

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros n e d que representam
        a fração.

        Exemplos:

        >>> frac = Fraction(2,5) # construtor chama __init__()
        >>> frac.num
        2
        >>> frac.den
        5
        >>> f01 = Fraction() # construtor chama __init__()
        >>> f01.num
        0
        >>> f01.den
        1
        """
        if d == 0:
            raise ValueError("O denominador não pode ser zero")

        self.put(n, d)  # put é um método da própria classe

    def __str__(self):
        """(Fraction) -> str
        Recebe uma referencia `self` a um objeto da classe Fraction e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe

        Exemplos:

        >>> frac = Fraction(2,5)
        >>> frac.__str__()
        '2/5'
        >>> print(frac)
        2/5
        """
        _mdc = mdc(self.num, self.den)

        return f"{self.num // _mdc}/{self.den // _mdc}"

    def get(self):
        """ (Fraction) -> int, int
        Recebe uma referência `self` a um objeto da classe Fraction e
        retorna a tupla formada pelo seu numerador (em self.num) e
        denominador (em self.den).
        """
        _mdc = mdc(self.num, self.den)

        return self.num // _mdc, self.den // _mdc

    def put(self, n, d):
        """ (Fraction, int, int) -> None
        Recebe uma referência `self` e dois inteiros, n e d, e
        carrega os atributos self.num e self.den com esses valores.
        """
        self.num = n
        self.den = d

    def mul(self, other):
        """ (Fraction, Fraction) -> Fraction
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da multiplicação self * other
        """
        # variáveis locais para simplificar o código
        # essas variáveis NÃO SÃO atributos
        sn, sd = self.get()  # get é um método da própria classe
        on, od = other.get()
        # calcula o novo numerador e denominador.
        # usando as variáveis locais é mais difícil esquecer o "self."
        num = sn * on
        den = sd * od
        # cria e retorna uma nova fração com o resultado
        return Fraction(num, den)

    def div(self, other):
        """ (Fraction, Fraction) -> Fraction
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da divisão self / other
        """
        sn, sd = self.get()
        on, od = other.get()

        num = sn * od
        den = sd * on

        return Fraction(num, den)

    def add(self, other):
        """ (Fraction, Fraction) -> Fraction
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da soma self + other
        """
        sn, sd = self.get()
        on, od = other.get()

        den = sd * od
        num = sn * od + on * sd

        return Fraction(num, den)

    def sub(self, other):
        """ (Fraction, Fraction) -> Fraction
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da subtração self - other
        """
        sn, sd = self.get()
        on, od = other.get()

        den = sd * od
        num = sn * od - on * sd

        return Fraction(num, den)


# ===================================================================
# Parte II: Uso da classe Fraction
# ===================================================================

def HFmaior(n):
    """ (int) -> Fraction

    Recebe um número inteiro positivo e retorna o número harmônico
    de ordem n. O número harmônico é calculado somando do maior
    para o menor termo. Retorna objeto tipo Fraction.
    """
    frac = Fraction(1, 1)
    for i in range(2, n + 1):
        frac_somar = Fraction(1, i)
        frac = frac.add(frac_somar)

    return frac


# ===================================================================

def HFmenor(n):
    """ (int) -> Fraction
    Recebe um número inteiro positivo e retorna o número harmônico
    de ordem n. O número harmônico é calculado somando do menor para
    o maior termo. Retorna objeto tipo Fraction.
    """
    frac = Fraction(1, n)
    for i in range(n - 1, 0, -1):
        frac_somar = Fraction(1, i)
        frac = frac.add(frac_somar)

    return frac


# ===================================================================
#  Escreva a seguir outras funções que desejar
# ===================================================================

def mdc(m, n):
    """
    (int, int) -> int
    """
    resto = m % n
    if resto == 0:
        return n
    return mdc(n, resto)


# =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
# =============================================================
if __name__ == "__main__":
    main()
