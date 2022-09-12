# -*- coding: utf-8 -*-
"""
    Atividade 06 - classe Horario

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: N

    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Gustavo Valencio Tofolo
    - Vicenzo Carlim de Sousa
    - João Victor Talma Gomes de Jesus

"""


def main():
    print("Testes da classe Horario\n")

    t1 = Horario(8, 0, 0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1, 40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0, 100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00')

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 > t2} e deve ser True')
    print(f't1 <  t2 é {t1 < t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23, 59, 59)
    t6 = Horario(25, 0, 1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 01:00:00')

    t8 = t1 - t2
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1  ##   nao temos horarios negativos nesse exercício
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')


class Horario:
    """
    Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.

       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve permitir os "comportamentos" ilustrados no enunciado.
    """

    # ------------------------------------------------------------------------------
    # INSIRA OUTROS MÉTODOS DA CLASSE HORARIO AQUI
    # ------------------------------------------------------------------------------

    def __init__(self, hora=0, minuto=0, segundo=0):
        self.dados = [hora, minuto, segundo]

        if segundo > 59:
            self.dados[1] = minuto + segundo // 60
            self.dados[2] = segundo % 60

        if self.dados[1] > 59:
            self.dados[0] = hora + self.dados[1] // 60
            self.dados[1] = self.dados[1] % 60

        self.dados[0] = self.dados[0] % 24

    def __str__(self):
        str_h = self.dados[0]
        if str_h < 10:
            str_h = '0' + f'{str_h}'

        str_m = self.dados[1]
        if str_m < 10:
            str_m = '0' + f'{str_m}'

        str_s = self.dados[2]
        if str_s < 10:
            str_s = '0' + f'{str_s}'

        return f"{str_h}:{str_m}:{str_s}"

    def __eq__(self, other):
        return self.dados[0] == other.dados[0] and self.dados[1] == other.dados[1] and self.dados[2] == other.dados[2]

    def __lt__(self, other):
        return self.dados[0] < other.dados[0] or (
                self.dados[0] == other.dados[0] and self.dados[1] < other.dados[1]) or (
                       self.dados[0] == other.dados[0] and self.dados[1] == other.dados[1] and self.dados[2] <
                       other.dados[2])

    def __qt__(self, other):
        return self.dados[0] > other.dados[0] or (
                self.dados[0] == other.dados[0] and self.dados[1] > other.dados[1]) or (
                       self.dados[0] == other.dados[0] and self.dados[1] == other.dados[1] and self.dados[2] >
                       other.dados[2])

    def __add__(self, other):
        if type(other) == Horario:
            return Horario(
                self.dados[0] + other.dados[0],
                self.dados[1] + other.dados[1],
                self.dados[2] + other.dados[2]
            )
        elif type(other) == int:
            return Horario(
                self.dados[0] + other
            )
        else:
            f_horario = trata_hora(other)

            return Horario(
                self.dados[0] + f_horario.dados[0],
                self.dados[1] + f_horario.dados[1],
                self.dados[2] + f_horario.dados[2]
            )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if other > self:
            return Horario()

        if type(other) == Horario:
            if self.dados[1] == 0 and other.dados[1] != 0:
                self.dados[0] -= 1
                self.dados[1] = 60

            return Horario(
                self.dados[0] - other.dados[0],
                self.dados[1] - other.dados[1],
                self.dados[2] - other.dados[2]
            )
        elif type(other) == int:
            return Horario(
                self.dados[0] - other
            )
        else:
            f_horario = trata_hora(other)

            if f_horario > self:
                return Horario()

            return Horario(
                self.dados[0] - f_horario.dados[0],
                self.dados[1] - f_horario.dados[1],
                self.dados[2] - f_horario.dados[2]
            )

    def __rsub__(self, other):
        return self - other

    # ------------------------------------------------------------------------------
    #     FIM DA CLASSE HORARIO
    # ------------------------------------------------------------------------------


# ===================================================================
#  Insira as funções que desejar aqui. CUIDADO com a tabulação.
# ===================================================================

def h_min(seq):
    menor = seq[0]
    for h in seq[1:]:
        if h < menor:
            menor = h

    return menor


def trata_hora(f):
    hora = int(f)
    float_part = f - int(f)
    minutos = float_part * 60
    segundos = (minutos - int(minutos)) * 60

    return Horario(
        hora, minutos, segundos
    )


if __name__ == '__main__':
    main()
