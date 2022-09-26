"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

vendas = [0, 0, 0, 0, 0]
ilhas = ['Faial', 'pico', 'sao_jorge', 'graciosa', 'terceira']

if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        for x in range(0, len(ilhas)):
            vendas[x] = int(input(f'vendas {ilhas[x]}'))




        continuar = input('Quer contunuar? [s, n]')
    print(f'Adeus!')
