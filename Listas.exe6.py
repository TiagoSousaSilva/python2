from math import factorial
"""
def conta(numero):
    while True:
        lista_n = []
        vezes = numero
        if vezes > 0:
            total = numero * (vezes - 1)
            vezes = vezes - 1
            lista_n.append(total)
            print(lista_n)
            break
    return total
"""
def factorial(numero):
    fact = 1
    if numero < 0:
        print('Numeros negativos sao inválidos.')
    else:
        for n in range(1, numero + 1):
            fact = fact * n

    return fact

if __name__ == '__main__':
    numero = int(input('Insira o numero: '))
    fact = 1
    if numero < 0:  #feito na def
        print('Numero fatoriais nao podem ser negativos.')
    else:
        for n in range(1, numero + 1):
            fact = fact * n

    print(f"A fatorial do numero {factorial(numero)}")