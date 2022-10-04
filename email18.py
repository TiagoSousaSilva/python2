"""
Escreva um programa que lê um número inteiro e determina quantas vezes
aparecem dois zeros seguidos. Por exemplo:
Escreva um inteiro
? 98007640003
O numero tem 3 zeros seguidos
"""

def zeros_seguidos(num):
    z = 0
    for x in range(len(num)):
        if num[x] == 0 and num[x + 1] == 0:
            z = z + 1

    return z


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':

        numeros = []
        numeros2 = []

        numero = input('Insira o numero: ')

        numeros = list(numero)

        for x in range(len(numeros)):
            conversao = int(numeros[x])
            numeros2.append(conversao)


        print(f'Verficação: {numeros2}')

        print(f'O numero de zeros seguidos é: {zeros_seguidos(numeros2)}')


        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break

