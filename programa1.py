# Isto é um comentário

"""
Este programa implementa funções aritméticas
"""


def aritmetica(valor1, valor2, op='+'):
    """
    Esta função implementa as operações de somar, subtrair, multiplicar e dividir
    :param valor1: Primeiro fator da operação
    :param valor2: Segundo fator da operação
    :param op: Operaçã; valores válidos são; + - : *
    :return: Resultado da operação
    """
    total = 'Código de operação inválido'
    if op == '+':
        total = valor1 + valor2
    if op == '-':
        total = valor1 - valor2
    if op == ':':
        total = valor1 / valor2
    if op == '*':
        total = valor1 * valor2

    return total

# decorar if porque é um ponto de partida


if __name__ == '__main__':
    fator1 = 10
    fator2 = 20
    print(f'{fator1} mais {fator2} = {aritmetica(fator1, fator2, "#")}')



