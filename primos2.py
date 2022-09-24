def primos(num1, num2):
    zeros = 0
    for n in range(num1, num2 + 1):  # sem o -1 o programa começa 1 numero á frente
        if n > 1:
            for i in range(2, n):
                if (i % n) == 0:
                    zeros += 1
    return zeros

if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Insira um número: '))
        num2 = int(input('Insira um número: '))
        if primos(num1, num2) == 0:  #o programa tem sempre 1 e se entre o espaço n tiver primos vais sempre para o 'else'
            print(f'Entre o espaço {num1, num2} não existem numeros primos.')
        else:
            print(f'Entre o espaço {num1, num2} existem {primos(num1, num2)} numeros primos.')
            print()
        continuar = input('Quer contunuar? [s, n]')
    print(f'Adeus!')