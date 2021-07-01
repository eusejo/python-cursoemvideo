print('===== DESAFIO 052 =====')

num = int(input('digite um numero: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[33m',end='')
    else:
        print('\033[31m',end='')
    print(f'{c} ', end='')
print(f'\n\033[mo numero {num} foi divido {tot} vez')

if tot == 2:
    print(f'por isso o numero {num} é primo')
else:
    print('por isso ele não é primo')
