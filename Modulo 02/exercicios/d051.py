print('===== DESAFIO 051 =====')

t1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))

s = 0

for c in range(t1, t1+10, r):
    s += c
print(s)