print('===== DESAFIO 034 =====')
s = float(input('qual o seu salario: '))
if s > 1250:
    a = s * (10/100)
    print(f'o seu aumento de 10% é de {s + a}')
else:
    a = s * (15/100)
    print(f'o seu aumento de 10% é de {s + a}')
