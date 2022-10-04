"""
Escreva um programa que lê um número e cria uma capicua cuja primeira
metade é o número lido. Por exemplo:
Escreva um número
-> 347
347743
"""

if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':

        numeros = []

        num1 = input('Insira o numero: ')

        num2 = num1[::-1]

        numeros.append(num1)
        numeros.append(num2)

        numeros2 = "".join([str(i) for i in numeros])


        print(numeros2)

        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break