print('===== DESAFIO 060 =====')

n = float(input('digite um numero: '))
f = 1

print('escolha com qual laço vc queria fazer')
print('[1] while   [2] for')
op = int(input('=> '))

if op == 1:
    while n > 1:
        f = f*n
        n -= 1
    print(f)