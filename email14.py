"""
14. Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
"""

if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':

        numero_int = input('Insira o numero inteiro: ')

        lista_numero = list(numero_int)
        ls_numero = []
        total = 0

        for x in range(len(lista_numero)):
            conversao = int(lista_numero[x])
            ls_numero.append(conversao)

        for x in range(len(ls_numero)):
                total += ls_numero[x]


        print(f'A lista do numero: {ls_numero}')

        print(f'A soma da lista é: {total}')


        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N' or 'n':
            break