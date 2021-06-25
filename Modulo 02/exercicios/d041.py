print('===== DESAFIO 041 =====')

nascimento = int(input('Digite o ano q vc nasceu: '))
idade = 2021 - nascimento

print(f'vc tem {idade} anos')

if idade <= 9:
    print('vc é um nadador mirim')
elif idade > 9 and idade <= 14:
    print('vc é um nadador infantil')
elif idade > 14 and idade <= 19:
    print('vc é um nadador junior')
elif idade > 19 and idade <= 20:
    print('vc é um nadador senior')
elif idade > 20:
    print('vc é um nadador master')