"""
6. Escreva um programa em Python que lê três números e que diz qual o
maior dos números lidos.
"""

def comparacao(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        total = num1
    if (num2 > num1) and (num2 > num3):
        total = num2
    if (num3 > num1) and (num3 > num2):
        total = num3

    return total

while __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Insira o primeiro numero: '))
        num2 = int(input('Insira o segundo numero: '))
        num3 = int(input('Insira o terceiro numero: '))
        print(f'O numero maior é: {comparacao(num1, num2, num3)}')
        continuar = input('Quer continuar? [s, n] ')
    print('Adeus!')