print('===== 061 =====')

t1 = float(input('digite o primeiro termo: '))
r = float(input('digite a razão: '))

cont = 1
t = t1

while cont <= 10:
    print(f'{int(t)}', end=' ')
    cont += 1
    t += r
print('FIM')
