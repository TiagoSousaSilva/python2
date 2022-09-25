"""
2. Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em Km) e o tempo necessário para a percorrer (em
minutos), e calcula a velocidade média em:
(a) Km / h
(b) m/s
"""

def VelMedKM(Num1, Num2):
    Num2 = Num2 / 60
    Total = Num1 / Num2

    return Total

def VelMedM(Num1, Num2):
    Num1 = Num1 * 1000
    Num2 = Num2 * 60
    Total = Num1 / Num2

    return Total



if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        num1 = int(input('Quantos kms tem a distância? '))
        num2 = int(input('Quantos mins demorou a percorrer? '))
        print(f'A velocidade média é {VelMedKM(num1, num2)} K/H e {VelMedM(num1, num2)} M/S')
        continuar = input('Quer continuar? [s, n] ')
    print('Adeus!')
