print('===== DESAFIO 028 =====')
import random
num = random.randint(0, 5)
t = int(input('qual foi o numero escolhido: '))
if t == num:
    print('parabens vc acertou')
else:
    print('perdeu')
