print('===== DESAFIO 074 =====')

from random import randint

maior = menor = 0
numeros = ()
for c in range(0, 5):
    num = randint(0, 20)
    numeros += (num,)
print(f'os numeros gerados foram: {numeros}')

print(f'o maior numero é {max(numeros)} e o menor é {min(numeros)}')