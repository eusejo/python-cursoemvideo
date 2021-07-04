n = 0
pares = impa = 0
while n != 0:
    n = int(input('digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impa += 1
print('cabo!')
print(f'foram digitados {pares} numeros pares e {impa} numeros impares')
