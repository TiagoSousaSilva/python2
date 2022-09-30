pessoa = (1, 'Maria', {'morada': 'rua de cima, 1', 'op': 9500}, 12.50) #tupple

meses ={'Janeiro', 'Fevereiro', 'Março'} #set

if __name__ == '__main__':
    print(pessoa[2]['op'])
    print(pessoa[2].keys())
    print(pessoa[2].values())
    print()

    for k in pessoa[2].keys():
        print(k)
    print()

    for v in pessoa[2].values():
        print(v)
    print()

    for k in pessoa[2].keys():
        print(f'{k} = {pessoa[2][k]}')

    meses.add('Abril')
    print(meses)
    meses.pop()
    print(meses)