print('===== DESAFIO 063 =====')

n = int(input('digite um valor: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    count+=1
print('-> fim')
