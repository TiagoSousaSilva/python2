"""
1. Escreva um programa em Python que pede ao utilizador que lhe forneça
dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).
O seu programa deve gerar uma interação como a seguinte:
Vou pedir-lhe dois numeros
Escreva o primeiro numero, x = 5
Escreva o segundo numero, y = 6
O valor de (x + 3 * y) * (x - y) e: -23
"""


def calculo(Num1, Num2):
    total = (Num1 + 3 * Num2) * (Num1 - Num2)

    return total


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        num1 = int(input('1º num: '))
        num2 = int(input('2º num: '))

        print(f'{calculo(num1, num2)}')

        continuar = input('Quer continuar? [s, n] ')
    print('Adeus!')
