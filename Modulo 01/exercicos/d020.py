print('===== DESAFIO 020 =====')
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
list = [n1, n2, n3, n4]
print('----- ordem do alunos -----')
print(f'primeiro: {random.choice(list)}')
print(f'segundo: {random.choice(list)}')
print(f'terceiro: {random.choice(list)}')
print(f'quarto: {random.choice(list)}')