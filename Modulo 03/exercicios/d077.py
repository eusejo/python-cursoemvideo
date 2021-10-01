print('===== DESAFIO 075 =====')

tupla = ('lapis', 'caneta',
    'senhor', 'mouse', 'teclado',
    'controle', 'televisao', 'copo'
)

for p in tupla:
    print(f'\nna palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')