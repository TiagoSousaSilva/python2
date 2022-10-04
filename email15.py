"""
Escreva um programa que lê uma série de dígitos (terminando com -1) e
calcula o inteiro que tem esses dígitos. Por exemplo, lendo os dígitos 1 5
4 5 8 -1, calcula o número inteiro 15458.
"""

if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        numeros = []
        while True:
            n = int(input('Numero: '))
            if n != -1:
                numeros.append(n)
            if n == -1:

                numero = "".join([str(i) for i in numeros])

                numero_int = int(numero)

                print(f'O número é: {numero_int}')
                print(f'A lista escolhida é: {numeros}')

                break

        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break