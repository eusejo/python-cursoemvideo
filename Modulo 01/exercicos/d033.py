print('===== DESAFIO 033 =====')
n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))
if (n1 > n2) and (n1 > n3):
    print(f'{n1} é o mairo numero')
elif (n2 > n1) and (n2 > n3):
    print(f'{n2} é o maior numero')
else:
    print(f'{n3} é o maior numero')
