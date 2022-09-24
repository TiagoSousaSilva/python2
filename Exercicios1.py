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
        for primos in range(num1, num2 + 1):
            if primos > 1:
                for n in range (2, primos):
                    if (primos % n) == 0:
                        break
                else:
                    print(primos)


while True:
    Num1 = int(input('Insira o 1ºnum: '))
    Num2 = int(input('Insira o 2ºnum: '))
    print(f'Os numeros primos entre {Num1} e {Num2} sao {primos}')

