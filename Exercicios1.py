"""
1.Pede ao utilizador 2 numeros. O 2º numero deve ser >= 1º
Mostra todos os numeros primos que há entre o primeiro e o segundo numero
depois de mostrar os numeros diz quantos numeros primos havia

// criar lista, tirar os numeros, dividor e mostrar //

2.Pede ao utilizador um numero inicial
pede ao utilizador um numero que representa "quantos"
Mostra aquela quantidade de numeros primos a partir do numero inicial
"""

def primos(num1, num2, op):
        primos = 0
        numero = range
        for n in range(num1, num2 + 1):
            op = range % n
            if op == 2:
                primos += 1  # zeros = zeros + 1
        return primos


while True:
    Num1 = int(input('Insira o 1ºnum: '))
    Num2 = int(input('Insira o 2ºnum: '))
    lista = range
    if primos(range) == 2:
        print(f'O numero tem {lista}')
    else:
        print('Não há primos')
    print(f'Tem {primos}')
