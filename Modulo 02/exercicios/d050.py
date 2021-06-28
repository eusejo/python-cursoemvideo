print('===== DESAFIO 050 =====')

s = 0

for c in range(0, 6):
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        s += n
print(f'o somatorio de todos esses valores pares é {s}')
