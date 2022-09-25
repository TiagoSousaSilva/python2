"""
3. Escreva um programa em Python que pede ao utilizador que lhe forneça

um inteiro correspondente a um número de segundos e que calcula o nú-
mero de dias correspondentes a esse número de segundos. O seu programa

deve permitir a interação:
Escreva um número de segundos
? 65432998
O número de dias correspondentes é 757.3263657407407
"""

def dias(num1):
    total = num1 / 60 / 60 / 24

    return total

def horas(num1):
    total = num1 / 60 / 60

    return total


def minutos(num1):
    total = num1 / 60

    return total


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        seg = int(input('Insira o número de segundos: '))
        print(f'O numero de dias é {dias(seg)} dias, {horas(seg)} horas e {minutos(seg)} minutos.')
        continuar = input('Quer continuar? [s, n] ')
    print('Adeus!')