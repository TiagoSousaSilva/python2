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

"""
Resolução:
def divisores(num):
    zeros = 0
    for n in range(1, num + 1)
        if num % n == 0:
            zeros += 1
    return zeros
    
    
if __name = '__main__':
    continuar = 's'
    while continuar == 's'
        ini = int(input('Insira o numero inicial '))
        fin = int(input('Insira o numero final '))
        primos = 0
        # TPC Alterar o for para um while com for dentro ( meu ex) e so com whiles
        for n in range(ini, fin + 1):
            if divisores(n) == 2:
                primos += 1
        print(f' Entra {ini} e {fim} há {primos} de primos.')
        continuar = input('Repetir [s | n] ')
    print(f'adeus')
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
        print('Bom \ndia')
        print('Bom \tdia')

        #exemplo nome
        nome = input('Nome: ')
        nl = nome.split(' ')
        print(f'On ome tem {len(nl)} palavras.')
        print(nl[0])


        for n in nl:
            print(n)

        x = 0
        while x < len(nl):
            print(nl[x])
            x += 1



        num1 = int(input('Insira um número: '))
        num2 = int(input('Insira um número: '))
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

