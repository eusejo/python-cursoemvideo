print('===== DESAFIO 019 =====')
import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
list_alu = [n1, n2, n3, n4]
sorteado = random.choice(list_alu)
print(f'o aluno sorteado foi: {sorteado}')