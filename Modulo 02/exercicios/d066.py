print('===== DESAFIO 066 =====')

count = s = 0

while True:
    n = int(input('digite um valor: '))
    count += 1
    if n == 999:
        count -= 1
        break
    s += n
print(f'a soma dos {count} valores foi {s}')