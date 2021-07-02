print('===== DESAFIO 054 =====')

tot = 0

for c in range(1, 8):
    nascimento = int(input(f'em que ano a {c} pessoa nasceu: '))
    if(2021 - nascimento >= 21):
        tot += 1
print(f'{tot} pessoas são maiores de idade')
print(f'{7 - tot} pessoa ainda não são maior de idade')
