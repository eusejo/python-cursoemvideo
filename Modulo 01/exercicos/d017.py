print('===== DESAFIO 017 =====')
from math import pow, sqrt
co = float(input('digite um cateto: '))
ca = float(input('digite o outro cateto: '))
hi = sqrt(pow(co, 2) + pow(ca, 2))
print(f'a hipotenusa do triangulo vale: {hi}')