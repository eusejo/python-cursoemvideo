print('===== DESAFIO 057 =====')

c = 1

while c != 0:
    sexo = str(input('digite o seu sexo: ')).upper().strip()[0]
    if sexo not in 'FMfm':
        print('erro')
    else:
        c = 0
print('cabo')
