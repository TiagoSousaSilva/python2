"""
fazer alteraçao de soma entre os primeiros numeros das duas listas
"""


if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55]
    ]


    for x in range(2):  ##Esta ao contrario pois queremos o y e este deve estar o topo
        for y in range(5): ##para conseguir imprimir 5 vezes
            total = vendas[0][y] + vendas[1][y]
            print(f'A soma entre venda[{0}][{y}] + venda[{1}][{y}] = {total}')
            print(total)


## resoluçao


    for x in range(2):
        print(x)

    for y in range(5):
        total = 0
        for x in range(2):
            total = vendas[0][y] + vendas[1][y]
        print(f'x={0, 1} y={y}')
        print(total)