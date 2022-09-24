menor = 6
maior = 11

print('Os numeros primos entre', menor, 'and', maior, 'sao: ')

for num in range(menor, maior + 1):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                break
            else:
                print(num)