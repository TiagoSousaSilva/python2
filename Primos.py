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


lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
#for num in range(menor, maior + 1):
    #if num % 2 == 0:
        #zero =+ 1