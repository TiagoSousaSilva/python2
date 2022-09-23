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
# Int usado para numeros inteiros, str para numeros com letras e float para numeros com decimais


if __name__ == '__main__':
    nome = input('Como te chamas? ')
    while True:
        fator1 = float(input('Insira o primeiro número: '))
        fator2 = float(input('Insira o segundo número: '))
        operacao = input('Insira a operação [+ , - , : , *]: ')
        print(f'Olá {nome}, {fator1} {operacao} {fator2} = {aritmetica(fator1, fator2, operacao)}')
        continuar = input('Quer contunuar? [S, N]')
        if continuar == 'N':
            break
    print(f'Adeus {nome}!')

