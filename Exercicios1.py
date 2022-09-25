"""
1.Pede ao utilizador 2 numeros. O 2º numero deve ser >= 1º
Mostra todos os numeros primos que há entre o primeiro e o segundo numero
depois de mostrar os numeros diz quantos numeros primos havia

// criar lista, tirar os numeros, dividor e mostrar //

2.Pede ao utilizador um numero inicial
pede ao utilizador um numero que representa "quantos"
Mostra aquela quantidade de numeros primos a partir do numero inicial
"""
"""
        primo = 0
        for n in range(num1, num2 + 1):
            if n > 1:
                for i in range(2, n):
                    if (n % i) == 0:
                        primo += 1
                else:
                    print(primo)
        print(f'primo {primo}')
"""

def primos(num1, num2):
    zero = 0
    for num in range(num1, num2 + 1):   # sem o -1 o programa começa 1 numero á frente
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    zero =+ 1
    return zero






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
        for n in range(num1, num2 + 1):
            if n > 1:
                for i in range(2, n):
                    if (n % i) == 0:
                        break
                else:
                    print(n)
        continuar = input('Quer contunuar? [s, n]')
    print(f'Adeus!')

