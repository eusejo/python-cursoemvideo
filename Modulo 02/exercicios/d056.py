print('===== DESAFIO 056 =====')

idadem = 0
maisvelho = 0

print('''Escolha entre
[m] para masculino e [f] para feminino''')

for c in range(1, 5):
    print('-'*10)
    nome = str(input('digite o seu nome: '))
    idade = int(input('digite a sua idade: '))
    sexo = str(input('digite o seu sexo: '))
    idadem += idade
    
print(f'a media de idade do grupo é {idadem/4}')
print(f'')
