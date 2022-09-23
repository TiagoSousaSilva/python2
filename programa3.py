def par(numero):
    if numero % 2 == 0:  ##ou num = numero % 2 // if num == 0 // return True
        return True
    else:
        return False


if __name__ == '__main__':
    nome = input('Como te chamas? ')
    continuar = 's'
    while continuar == 's':
        num = int(input('Insira um número '))
        if par(num):
            print(f'O número {num} é par')
        else:
            print(f'O número {num} é ímpar.')
        continuar = input('Repetir [s | n] ')
    print(f'Adeus {nome}!')
