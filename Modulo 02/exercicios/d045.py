print('===== DESAFIO 045 =====')

import random
import time
print('\033[35m===== Jodo massa =====\033[m')

print('''Escolha entre:
[*] Pedra
[*] Papel
[*] tesoura''')

jogadas = [
    'pedra',
    'papel',
    'tesoura'
]
computador = random.choice(jogadas)

jogada = str(input('qual a sua jogada: '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print('-='*10)
print(f'vc escolheu {jogada}')
print(f'o pc escolheu {computador}')
print('-='*10)

if computador == 'pedra' and jogada == 'papel':
    print('\033[32mparabens vc ganhou\033[m')
elif computador == 'pedra' and jogada == 'tesoura':
    print('\033[31mvc perdeu\033[m')
elif computador == 'pedra' and jogada == 'pedra': 
    print('deu empate')
elif computador == 'tesoura' and jogada == 'pedra':
    print('\033[32mparabens vc ganhou\033[m')
elif computador == 'tesoura' and jogada == 'papel':
    print('\033[31mvc perdeu\033[m')
elif computador == 'tesoura' and jogada == 'tesoura':
    print('deu empate')
elif computador == 'papel' and jogada == 'tesoura':
    print('\033[32mparabens vc ganhou\033[m')
elif computador == 'papel' and jogada == 'pedra':
    print('\033[31mvc perdeu\033[m')
elif computador == 'papel' and jogada == 'papel':
    print('deu empate')
