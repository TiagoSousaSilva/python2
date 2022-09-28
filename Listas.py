"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha
Exemplo da estrutura de armazenamento das vendas:
    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]
    ou então:
    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]
"""

if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55]
    ]

    print(vendas)

    for venda in vendas:
        print(venda)
        for v in venda:
            print(v)

    x = 0 # numero da lista
    y = 0 # numero da coluna
    print(f'vendas[x][y]={vendas[x][y]}') # numero do x/y

    for x in range(2):
        print(f'x={x}')

    for x in range(len(vendas)):
        for y in range(len(vendas[0])):
            print(f'venda[{x}][{y}]={vendas[x][y]}')

    print()
    for x in range(2):
        for y in range(5):
            print(f'venda[{x}][{y}]={vendas[x][y]}')
            print('xxx')  # executado 10 vezes
        print('xxx')  # executado 2 vezes

    # total de vendas
    total_vendas = 0
    for x in range(2):
        total_linha = 0
        for y in range(5):
            #print(f'vendas[{x}][{y}]= {vendas[x][y]}')
            total_vendas = total_vendas + vendas[x][y]
            total_linha = total_linha + vendas[x][y]
        print(f'total_linha={total_linha}') #1 linha é a soma da 1º lista
    print(f'total_vendas={total_vendas}')