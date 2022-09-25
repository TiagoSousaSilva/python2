"""
1.Pede ao utilizador 2 numeros. O 2º numero deve ser >= 1º
Mostra todos os numeros primos que há entre o primeiro e o segundo numero
depois de mostrar os numeros diz quantos numeros primos havia

// criar lista, tirar os numeros, dividor e mostrar //

2.Pede ao utilizador um numero inicial
pede ao utilizador um numero que representa "quantos"
Mostra aquela quantidade de numeros primos a partir do numero inicial
"""

def divisores(num, dist):
    zeros = 0
    for num in range(num, dist + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    zeros += 1
    return zeros


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        numero = int(input('Insira um número: '))
        primos = int(input('Quantos numeros primos quer? '))

        continuar = input('Quer contunuar? [s, n]')
    print(f'Adeus!')