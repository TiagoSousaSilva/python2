##Converter a nota de numero para letra
##[A, 80-100; B,60-79; C, 40-59; D, 20,39; E, 0-19]

while True:
    nota = int(input('Insere a tua nota: '))

    if nota >= 80 and nota <= 100:
        print('Tiveste um A.')

    if nota >= 60 and nota <= 79:
        print('Tiveste um B.')

    if nota >= 40 and nota <= 59:
        print('Tiveste um C.')

    if nota >= 20 and nota <= 39:
        print('Tiveste um D.')

    if nota >= 0 and nota <= 19:
        print('Tiveste um E.')

    if 0 < nota > 100:
        print('Número inválido!')

    continuar = input('Quer continuar? [S,N] ')
    if continuar == 'N' or continuar == 'n':
        break

