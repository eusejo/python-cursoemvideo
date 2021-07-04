print('===== DESAFIO 056 =====')

idadem = 0
maisvelho = 0
nomevelho = ''
totmulher = 0

print('''Escolha entre
[m] para masculino e [f] para feminino''')

for c in range(1, 5):
    print('-'*10)
    nome = str(input('digite o seu nome: '))
    idade = int(input('digite a sua idade: '))
    sexo = str(input('digite o seu sexo: '))
    idadem += idade
    if c == 1 and sexo in 'Mm':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
print(f'a media de idade do grupo é {idadem/4}')
print(f'o nome do homem mais velho é {nomevelho}')
