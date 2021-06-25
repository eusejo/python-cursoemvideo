print('===== DESAFIO 038 =====')

n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print('não existe maior, pois ambos são iguais')
