'''
AS TUPLAS SÃO 
IMTAVEIS

as tuplas podem
receber dados de
tipos diferentes

adicionando elementos na
tupla: tupla + novoelemento

sorted()
len()
index()
del()
'''

gay = (
    'hamburguer',
    'suco',
    'pudim',
    'pizza'
)
for c in gay:
    print(f'eu vou comer {c}')
print('to cheio')

num = (
    1,
    5,
    3,
    2,
    4
)
print(sorted(num)) # colocar em ordem

# juntando tuplas
a = (1, 2, 3)
b = (4, 5, 6, 7)
c = a+b
print(c)

pessoa = ()