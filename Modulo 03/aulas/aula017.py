'''
tuplas()
lista[]
AS LISTAS SÃO MUTAVEIS
DIFERENTE DAS TUPLAS

append(a)
insert(a,b) a - posição b - item novo
del(lista[])
pop(a)
remove(a)
sort() - sort(reverse=True)
'''

num = [3,5,7,9]
num[0] = 4
num.append(7)
num.sort()
print(num)

valores = []
valores.append(9)
valores.append(6)
valores.append(4)

for int in range(0, 4):
    valores.append(int(input('digite um valor: ')))

for c,v in enumerate(valores):
    print(f'na posição {c} encontrei o {v}')
print('fim')

# ligação entre listas
a = [2,3,4,7]
b = a
b[2] = 8
print(f'a lista A {a}')
print(f'a lista B {b}')

# copia de lista
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'a lista A {a}')
print(f'a lista B {b}')
