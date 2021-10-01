print('===== DESAFIO 075 =====')

tupla = ()
num = 0

for c in range(0, 4):
    num = int(input('digite um numero: '))
    tupla += (num,)
print(f'vc digitou os valores {tupla}')
print(f'o numero 9 aprece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o numero 3 esta na posição {tupla.index(3)}')
else:
    print('o valor 3 não foi digitado')
print('os numeros pares foram ', end="")
for c in tupla:
    if c % 2 == 0:
        print(c, end=" ")