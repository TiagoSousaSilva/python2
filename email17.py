"""
Dado um conjunto de n inteiros representando notas de alunos, escreva
um programa em Python para determinar quantos tiveram nota positiva.
Modifique o seu programa de modo a também calcular qual a percentagem
de notas positivas.
"""

def notas_positivas(x):
    z = 0
    for i in range(len(x)):
        if x[i] >= 50:
            z = z + 1

    return z

def percentagem_pos(x):
    z = 0
    comp = len(x)
    total = 0
    for i in range(len(x)):
        if x[i] >= 50:
            z = z + 1
    total = (z*100) / comp

    return total


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':

        lista_notas = []

        while True:

            notas = int(input('Notas por ordem (-1 para terminar): '))

            if notas != -1:
                lista_notas.append(notas)
            if notas == -1:
                break

        print(lista_notas)
        print(f'O numero de notas positivas é: {notas_positivas(lista_notas)}')
        print(f'A percentagem de positivas é: {percentagem_pos(lista_notas)}%')


        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break