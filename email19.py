"""
Escreva um programa em Python que lê uma quantia em Euros e calcula
o número de notas de 50 e, 20 e, 10 e, 5 e e moedas de 2 e, 1 e, 50
cêntimos, 20 cêntimos, 10 cêntimos, 5 cêntimos, 2 cêntimos e 1 cêntimo,

necessário para perfazer, essa quantia, utilizando sempre o máximo nú-
mero de notas e moedas para cada quantia, da mais elevada, para a mais

baixa.
"""

def notas(num):
    nota_50 = num / 50
    nota50_int = int(nota_50)

    nota_20 = (num - (nota50_int*50)) / 20
    nota20_int = int(nota_20)

    nota_10 = (num - (nota50_int*50) - (nota20_int*20)) / 10
    nota10_int = int(nota_10)

    nota_5 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10)) / 5
    nota5_int = int(nota_5)

    moeda_2 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5)) / 2
    moeda2_int = int(moeda_2)

    moeda_1 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5) - (moeda2_int*2)) / 1
    moeda1_int = int(moeda_1)

    moeda_050 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5) - (moeda2_int*2) - (moeda1_int*1)) / 0.50
    moeda050_int = int(moeda_050)

    moeda_020 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5) - (moeda2_int*2) - (moeda1_int*1) - (moeda050_int*0.50)) / 0.20
    moeda020_int = int(moeda_020)

    moeda_010 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5) - (moeda2_int*2) - (moeda1_int*1) - (moeda050_int*0.50) - (moeda020_int*0.20)) / 0.10
    moeda010_int = int(moeda_010)

    moeda_005 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5) - (moeda2_int*2) - (moeda1_int*1) - (moeda050_int*0.50) - (moeda020_int*0.20) - (moeda010_int*0.10)) / 0.05
    moeda005_int = int(moeda_005)

    moeda_002 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5) - (moeda2_int*2) - (moeda1_int*1) - (moeda050_int*0.50) - (moeda020_int*0.20) - (moeda010_int*0.10) - (moeda005_int*0.05)) / 0.02
    moeda002_int = int(moeda_002)

    moeda_001 = (num - (nota50_int*50) - (nota20_int*20) - (nota10_int*10) - (nota5_int*5) - (moeda2_int*2) - (moeda1_int*1) - (moeda050_int*0.50) - (moeda020_int*0.20) - (moeda010_int*0.10) - (moeda005_int*0.05) - (moeda002_int*0.02)) / 0.01
    moeda001_int = int(moeda_001)


    print(f'{nota50_int} nota/s de 50, {nota20_int} nota/s de 20, {nota10_int} nota/s de 10, {nota5_int} nota/s 5, {moeda2_int} moeda/s de 2, {moeda1_int} moeda/s de 1, {moeda050_int} moeda/s de 0.50, {moeda020_int} moeda/s de 0.20, {moeda010_int} moeda/s de 0.10, {moeda005_int} moeda/s de 0.05, {moeda002_int} moeda/s de 0.02 e {moeda001_int} moeda/s de 0.01.')

    return


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':

        numero = float(input('Insira o valor: '))

        print(f'{notas(numero)}')

        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N' or 'n':
            break


