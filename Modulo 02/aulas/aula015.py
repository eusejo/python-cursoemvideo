s = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s += n
print(f'a soma de todos os numeros é {s}')
