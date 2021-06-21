print('===== DESAFIO 031 =====')
p = int(input('qual a distancia da viagem em km: '))
if p >= 200:
    print(f'vc vai pagar {0.45 * p}')
else:
    print(f'vc vai pagar {0.50 * p}')
