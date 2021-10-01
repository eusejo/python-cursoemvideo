print('===== DESAFIO 073 =====')

times = ('corinthias', 'palmeiras', 'santos',
    'gremio', 'cruzeiro', 'flamengo', 'vasco',
    'chapecoense', 'atletico', 'bota fogo',
    'atletico-pr', 'bahia', 'são paulo', 'fluminense',
    'sport recife', 'ec vitoria', 'coritiba', 'avai',
    'ponte preta', 'atletico-go'
)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'os 5 primeiros são: {times[:5]}')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'os 4 ultimos são: {times[16:]}')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'os times em ordem alfabetica: {sorted(times)}')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'o chapecoense enta na {times.index("chapecoense")} posição')