print('===== DESAFIO 029 =====')
v = float(input('qual a velocidade do carro: '))
if v > 80:
    print('multado otario')
    print(f'vc vai pagar R${(v - 80) * 7}')
else:
    print('de boa')