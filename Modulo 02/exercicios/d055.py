print('===== DESAFIO 055 =====')

menor = 0
maior = 0

for p in range(1, 6):
    peso = float(input(f'digite o peso da {p} pessoa: '))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso foi de {maior}')
print(f'o menor peso foi de {menor}')
