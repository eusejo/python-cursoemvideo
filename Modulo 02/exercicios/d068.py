print('===== DESAFIO 068 =====')

from random import randint

print('-='*20)
print('vamos jogar par ou impar')
print('-='*20)

while True:
    computador = randint(0, 10)
    jogada = int(input('diga um valor: '))
    pi = str(input('par ou impart? [P/I] '))