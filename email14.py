"""
14. Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
"""


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        numero_int = input('Insira o numero inteiro: ')
        #convert number into digits
        #Put in a list
        #Sum list

        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break