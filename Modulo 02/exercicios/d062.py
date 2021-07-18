print('===== DESAFIO 062 =====')

t1 = float(input('digite o primeiro termo: '))
r = float(input('digite a razão: '))

cont = 1
t = t1

while cont <= 10:
    print(f'{int(t)}', end=' ')
    t += r
    cont += 1
print('\nvc dejesa mostrar mais quantos termos: ')
op = float(input('=+ '))
while op != 0:
    print(f'{t}', end=' ')
    t += r
    op -= 1
