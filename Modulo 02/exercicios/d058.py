print('===== DESAFIO 058 =====')

import random
p = random.randint(0, 10)
c = 1
t = 0

while c != 0:
    num = int(input('Adivinhe o numero que eu pensei: '))
    if num != p:
        print('errou!!')
        print('tente novamente')
    else:
        print('ACERTOU')
        print(f'o numero que eu pensei foi {p}')
        c = 0
    t += 1
print(f'vc tentou {t} vezes')
