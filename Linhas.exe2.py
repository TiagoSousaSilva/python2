"""
total de vendas de gasolinas, total de vendas de gasolio, e depois o total dos dois em cada ilha
imprimir 7 linhas total gasolina, gasolio, ilhas
        tipos = ['Gasolina', 'Gasoleo]
        ilhas = ['Faial', 'Pico', 'S. Jorge', 'Graciosa', 'Terceira']
            vendas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

"""
"""
Minha resoluçao
if __name__ == '__main__':
    tipos = ['Gasolina', 'Gasoleo']
    ilhas = ['Faial', 'Pico', 'S. Jorge', 'Graciosa', 'Terceira']

    colunas = int(input(f'Tamanho da lista é: '))
    vendas = []
    for x in range(colunas):
        vendas.append([int(y) for y in input('Ponha os valores separdos por espaço: ').split()])
    print(vendas)
"""


tipos = ['Gasolina', 'Gasoleo']
ilhas = ['Faial', 'Pico', 'S. Jorge', 'Graciosa', 'Terceira']
vendas = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]

if __name__ == '__main__':
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            while True:
                try:
                    vendas[x][y] = int(input(f'Insira vendas de {tipos[x]} para a ilha {ilhas[y]}'))
                    break
                except ValueError:
                    print(f'Insira um valor válido para vendas de {tipos[x]} na ilha {ilhas[y]}')
    print(vendas)

    #Imprimir vendas por tipo

    for x in range(len(vendas)):
        total = 0
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas para {tipos[x]} = {total}')



    #Imprimir vendas por ilha

    Z = 0
    for y in range(len(vendas[Z])):
        Z += 1
        total = 0
        for x in range(len(vendas)):
            total += vendas[x][y]
        print(f'Total de vendas para {ilhas[y]} = {total}')


