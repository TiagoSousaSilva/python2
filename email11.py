"""
Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
"""

if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        numero = input('Insira o numero para ser invertido: ')

        numero = numero[::-1]

        print(numero)

        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break