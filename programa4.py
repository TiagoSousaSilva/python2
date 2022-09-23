"""
Imprimir os números pares entre 1 e o numero inserido
"""
from programa3 import par

# range(start, stop, step)
if __name__ == '__main__':
    num1 = int(input('Insira o primeiro número: '))

    for x in range(1, num1 + 1):
        if par(x):
            print(x)


