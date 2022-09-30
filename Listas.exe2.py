"""
total de vendas de gasolinas, total de vendas de gasolio, e depois o total dos dois em cada ilha
imprimir 7 linhas total gasolina, gasolio, ilhas
        tipos = ['Gasolina', 'Gasoleo]
        ilhas = ['Faial', 'Pico', 'S. Jorge', 'Graciosa', 'Terceira']
            vendas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

vendas = [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
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

totais = [0, 0, 0, 0, 0]

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
        totais[y] = total

    # total de vendas

    total= 0
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            total += vendas[x][y]
    print(f'Total de vendas= {total}')


    # total de vendas de combustivel, onde se vendeu menos/mais


    maior = totais[0]
    menor = totais[0]
    for x in range(1, len(totais)):
        if totais[x] > maior:
            maior = totais[x]
        if totais[x] < menor:
            menor = totais[x]
#verificaçao    print(f'O numero maior é {maior} e o numero menor é {menor}')

    ilha_menor = []
    ilha_maior = []

    for x in range(len(totais)):
        if totais[x] == maior:
            ilha_maior.append(ilhas[x])
        if totais[x] == menor:
            ilha_menor.append(ilhas[x])

    print(totais)
    print(f'Ilha maior = {ilha_maior} = {maior} \nIlha menor = {ilha_menor} = {menor}')

#qual ilha consumiu Mais gasoleo e mais gasolina (nao os dois juntos)
"""
    venda_maior = 0
    venda_menor = 0

    for y in range(len(vendas[x])):
        for x in range(len(vendas)):
            if vendas[x] > venda_maior:
                venda_maior = vendas[x]
        print(venda_maior)
"""

