"""
Escreva um programa que:

1.     Pede ao utilizador para inserir uma frase

2.     Pede ao utilizador para inserir o texto que pretende substituir

3.     Pede ao utilizador para inserir o novo texto

4.     Apresenta a nova frase
"""


def frase_lista(frase):
    frase_list = frase.split()

    return frase_list

if __name__ == '__main__':
    continuar = 's' or 'S'
    frase = input('Insira a sua frase: ')
    while continuar == 's' or 'S':
        palavra = input('Insira a palavra para substituir a outra: ')
        mudar = input('Insira a palavra para substituir: ')

        if palavra in frase_lista(frase):
            frase = frase_lista(frase)
            for x in range(len(frase)):
                if frase[x] == palavra:
                    frase[x] = mudar
            frase = ' '.join(str(x) for x in frase)
            print(frase)
        else:
            print('A palavra nao está na frase.')

        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break
print(f'Adeus!')