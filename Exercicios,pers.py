"""
1. (maior menor igual)

2. 1º 2ºnº. for ou while?
Soma/ 2º num tem de ser maior q o 1º/ temos q ter numeros(leras n pode dar erros)

3(eu).escreve uma frase com mais de 10 caracteres: (input) *
 - Nao permitir mais do q 2 caracteres consecutivos iguais
 - Quantos caracteres de cada ( quantos As por ex.)
 - A frase termina obrigatóriamente com um . ! ? (parte da validação) *
"""

def conta_letras(frase):
    #frase.replace(' ', '') para retirar os espaços
    len(frase)
    return len(frase)


#def letras_seguidas(frase):
#    letras = 'qwertyuiopasdfghjklzxcvbnm'
#    frase.index(letras)


def letras_seguidas(x):
    return x


def seguidos(l1, l2):
    a = letras_seguidas(l1[0])
    b = letras_seguidas(l2[0])

    for i in range(1, len(l1)):
        if l1[i] != l1[i-1]:
            a += letras_seguidas(l1[i])
    for i in range(1, len(l2)):
        if l2[i] != l2[i-1]:
            b += letras_seguidas(l2[i])

    if a == b:
        return True
    return False



if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        letras = 'qwertyuiopasdfghjklzxcvbnm'

        frase = input('Escreve uma frase com mais de 10 caracteres: ')

        comp = len(frase)
        ult_cha = frase[comp - 1]
        print(ult_cha)

        while len(frase) < 10:
            print('A sua frase tem menos de 10 caracteres.')
            break

        if ult_cha != '.' and ult_cha != '?' and ult_cha != '!':
            print('A frase não tem pontuação.')
            break


        if seguidos(frase, letras):
            print('Há letras seguidas.')



        continuar = input('Quer contunuar? [s, n]')
    print(f'Adeus!')
