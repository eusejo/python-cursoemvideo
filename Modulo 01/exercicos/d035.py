print('===== DESAFIO 035 =====')
l1 = float(input('digite um lado: '))
l2 = float(input('digite outro lado: '))
l3 = float(input('digite mais um lado: '))
if (l1 < l2 + l3) and (l2 < l3 + l1) and (l3 < l1 + l2):
    print('o triangulo existe')
else:
    print('o triangulo não existe')
